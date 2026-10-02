param([string]$Site = (Join-Path $PSScriptRoot '../_site'))

$ErrorActionPreference = 'Stop'
$root = (Resolve-Path -LiteralPath $Site).Path
$failures = [System.Collections.Generic.List[string]]::new()
$htmlFiles = @(Get-ChildItem -LiteralPath $root -Filter '*.html' -Recurse)
$idCache = @{}

foreach ($required in @('index.html', '404.html', 'index.json', 'toc.json', 'navigation/toc.json', 'public/main.css', 'public/main.js', '.nojekyll')) {
    if (-not (Test-Path -LiteralPath (Join-Path $root $required) -PathType Leaf)) {
        $failures.Add("Missing generated file: $required")
    }
}

foreach ($file in $htmlFiles) {
    $relative = [IO.Path]::GetRelativePath($root, $file.FullName).Replace('\', '/')
    $html = Get-Content -LiteralPath $file.FullName -Raw
    $baseUri = [Uri]::new("https://docs.invalid/$relative")
    foreach ($match in [regex]::Matches($html, '(?i)\b(?:href|src)\s*=\s*["'']([^"'']+)["'']')) {
        $link = [Net.WebUtility]::HtmlDecode($match.Groups[1].Value)
        if ($link -match '^(?:[a-z][a-z\d+.-]*:|//)') { continue }
        $uri = [Uri]::new($baseUri, $link)
        $path = [Uri]::UnescapeDataString($uri.AbsolutePath).TrimStart('/')
        if ($path.EndsWith('/') -or $path -eq '') { $path += 'index.html' }
        $target = Join-Path $root $path
        if (-not (Test-Path -LiteralPath $target -PathType Leaf)) {
            $failures.Add("${relative}: missing target '$link'")
            continue
        }
        if ($uri.Fragment.Length -gt 1 -and $path.EndsWith('.html')) {
            if (-not $idCache.ContainsKey($target)) {
                $targetHtml = Get-Content -LiteralPath $target -Raw
                $ids = [System.Collections.Generic.HashSet[string]]::new([StringComparer]::Ordinal)
                foreach ($id in [regex]::Matches($targetHtml, '(?i)\bid\s*=\s*["'']([^"'']+)["'']')) {
                    [void]$ids.Add([Net.WebUtility]::HtmlDecode($id.Groups[1].Value))
                }
                $idCache[$target] = $ids
            }
            $fragment = [Uri]::UnescapeDataString($uri.Fragment.Substring(1))
            if (-not $idCache[$target].Contains($fragment)) {
                $failures.Add("${relative}: missing anchor '$link'")
            }
        }
    }
}

# Search and navigation are loaded at runtime and must resolve under a project subpath.
$search = Get-Content (Join-Path $root 'index.json') -Raw | ConvertFrom-Json -AsHashtable
foreach ($entry in $search.Keys) {
    if (-not (Test-Path -LiteralPath (Join-Path $root $entry) -PathType Leaf)) {
        $failures.Add("Search index: missing page '$entry'")
    }
}
if ($search.Count -lt 20) { $failures.Add('Search index contains fewer than 20 articles.') }

if ($failures.Count) {
    $failures | ForEach-Object { Write-Output $_ }
    throw "$($failures.Count) site validation error(s)."
}
Write-Output "Checked $($htmlFiles.Count) HTML files and $($search.Count) search entries: all local links, anchors, and assets resolve."
