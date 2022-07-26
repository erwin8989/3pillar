sed -i 's/80/8081/g' /etc/apache2/ports.conf && sed -i 's/80/8081/g' /etc/apache2/sites-enabled/000-default.conf && service apache2 restart && service apache2 status
