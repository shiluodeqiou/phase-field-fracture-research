$ErrorActionPreference = 'Stop'
$docx = 'E:\909 研究\相场文献和程序\参考文献\相场文献阅读进展与问题记录.docx'
$pdf  = 'E:\909 研究\相场文献和程序\参考文献\rendered_reading_log\相场文献阅读进展与问题记录.pdf'
$outDir = Split-Path -Parent $pdf
New-Item -ItemType Directory -Force -Path $outDir | Out-Null

$word = New-Object -ComObject Word.Application
try {
    $doc = $word.Documents.Open($docx)
    $doc.ExportAsFixedFormat($pdf, 17)
    $doc.Close()
    $word.Quit()
    Write-Output "PDF exported: $pdf"
} catch {
    try { $word.Quit() } catch {}
    throw
}
