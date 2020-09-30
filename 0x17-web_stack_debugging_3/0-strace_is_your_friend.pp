#puppet manifest to resolve WP 500 error

exec { 'modify php extension'
  command => "sed -i 's/phpp/php/g' /var/www/html/wp-includes/class-wp-locale.phpp"
  path    => '/bin'
}