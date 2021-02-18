domain='domain.com'
for i in $(ls -1 files | grep -E "*.pdf$")
do
    file=$(basename -- $i .pdf)
    echo "$file"
    python3 send_email.py "$file@$domain" $file
done