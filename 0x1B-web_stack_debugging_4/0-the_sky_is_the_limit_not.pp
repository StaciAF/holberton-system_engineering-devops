# adding Nginx limits
exec { 'correcting ULIMIT Nginx':
  command => "sed -i 's/ULIMIT=\"-n 15\"/ULIMIT=\"-n 4096\"/' /etc/default/nginx",
  path    => ['/usr/bin', '/bin', '/sbin']
} ~>
service { 'nginx':
  ensure => running
}
