# this manifest kills a process called killmenow with pkill
exec { 'killmenow':
  command => '/usr/bin/pkill -f killmenow'
}
