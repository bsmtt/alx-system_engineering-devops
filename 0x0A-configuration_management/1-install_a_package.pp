package { 'python3-pip':
  ensure => 'present',
}

pip_package { 'flask':
  ensure   => '2.1.0',
  provider => 'pip3',
}
