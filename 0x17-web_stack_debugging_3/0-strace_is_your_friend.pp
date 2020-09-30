#puppet manifest to resolve WP 500 error

exec { 'modify php extension':
  command => "sed -i 's/phpp/php/g' /var/www/html/wp-settings.php",
  path    => '/bin'
}