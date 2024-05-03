# kill a process named killmenow

exec { 'pkill killmenow' :
    provider => 'shell',
    command => 'pkill killmenow',
}
