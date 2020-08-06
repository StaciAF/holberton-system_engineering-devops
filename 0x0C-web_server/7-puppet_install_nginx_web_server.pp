# Configure server with Puppet
package { 'nginx':
  ensure   => installed,
  provider => 'apt',
}

service { 'nginx':
  ensure  => running,
  require => Package['nginx'],
}

file { '/var/www/html/index.html':
  ensure  => file,
  content => 'Holberton School',
}

file_line { '301 redirect':
  ensure => 'present',
  path   => '/etc/nginx/sites-available/default',
  line   => rewrite
  after  => /^server_name.*/,
}
