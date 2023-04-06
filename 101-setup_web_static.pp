# Check if Nginx is installed
package { 'nginx':
  ensure => installed,
}

# Create directories
file { ['/data', '/data/web_static', '/data/web_static/releases', '/data/web_static/shared', '/data/web_static/releases/test']:
  ensure => 'directory',
  owner  => 'ubuntu',
  group  => 'ubuntu',
  mode   => '0755',
}

# Create fake HTML file
file { '/data/web_static/releases/test/index.html':
  content => '<html><body>Hello world!</body></html>',
  owner   => 'ubuntu',
  group   => 'ubuntu',
  mode    => '0644',
}

# Create symbolic link
file { '/data/web_static/current':
  ensure => 'link',
  target => '/data/web_static/releases/test',
  owner  => 'ubuntu',
  group  => 'ubuntu',
  mode   => '0755',
}

# Update Nginx configuration
file { '/etc/nginx/sites-available/default':
  content => "server {
    listen 80;
    listen [::]:80 default_server;
    root   /etc/nginx/html;
    index  index.html index.htm;
    location /redirect_me {
        return 301 https://www.youtube.com/;
    }
    location /hbnb_static/ {
        alias /data/web_static/current/;
        index index.html;
    }
    error_page 404 /404.html;
    location /404 {
      root /etc/nginx/html;
      internal;
    }
    add_header X-Served-By \$hostname;
}",
  require => File['/data/web_static/current'],
  notify  => Service['nginx'],
}

# Restart Nginx
service { 'nginx':
  ensure    => running,
  enable    => true,
  subscribe => File['/etc/nginx/sites-available/default'],
}
