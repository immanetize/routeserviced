=============
routeserviced
=============

be confined no more, walled hosts

what does it do?
================
routeserviced is a daemon which fiddles routes and such if you poke it right.

how do i use it?
================
resources/20-routeserviced.rules must be deployed to /etc/polkit-1/rules.d/ , and polkit reloaded, for
routeserviced to manipulate interfaces.
