# this manifest configures a server with custom HTTP header response

exec { 'apt-update':
  command => '/usr/bin/env apt-get -y update'
}

package { 'nginx':
  require => Exec['apt-update'];
  ensure  => installed,
}

file { '/etc/nginx/nginx.conf':
  ensure  => file,
  content => 'add_header X-Served-By 1698-web-01',
  require => Package['nginx'],
}

service { 'nginx':
  ensure  => running,
  restart => 'sudo service nginx restart'
}
