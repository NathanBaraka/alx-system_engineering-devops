#command execution
exec { 'pkill killmenow':
	path => '/usr/bin:/usr/sbin:/bin'
}

