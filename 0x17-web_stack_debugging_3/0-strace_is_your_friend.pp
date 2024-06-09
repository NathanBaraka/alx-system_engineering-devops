<<<<<<< HEAD
# This Fixes bad `phpp` extensions to the correct `php` and in the WordPress file `wp-settings.php`.
=======
# This code Fixes bad `phpp` extensions to `php` in the WordPress file `wp-settings.php`.
>>>>>>> 772a107025d6b413eb5ca97f2e068bc21566f86a

exec { 'fix-wordpress':
  command => 'sed -i s/phpp/php/g /var/www/html/wp-settings.php',
  path    => '/usr/local/bin/:/bin/'
}
