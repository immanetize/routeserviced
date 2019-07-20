plan
----
- accepts authenticated api requests from the network to implement firewall changes
- routesets are intended to provide controlled network access to a specific resource 
  outside normal network boundaries
- you probably overrode dns records if you are using this
- DNAT/SNAT behavior for any number of specific ports or port groups
- routesets pushed via dbus api to firewalld (enables platform-level auditing)
- aware of peers, each route has master/standby designations
- can coordinate master change on demand or failure
- plugin structure for events
- node can test/monitor viability of route in standby
- route plugin structure
  - when applying route, test potential endpoints and choose
  - apply "bring-up" scripts (to become integrated features please)
  - load balance output?
  - healthcheck
- ipsets!
- query/report existing routesets 
- accounting for packet consumption of a routeset
- authentication plugins
  - flat file
  - ldap
  - some password file database thing
  - kubernetes plugin
  - gssapi
- owners can instantiate change, triggering re-runs of automation
- may need to bring up "front side" address when bringing up ruleset
- interface configuration via dbus api to networkmanager
- interfaces are independent of rulesets; rulesets depend on them but do not own them.
- an implementation *may* bring up an undefined interface via inference from ruleset
  if the interface plugin permits
   ::
   ruleset:
      name: myruleset
       - outside_bind: [any named_interface { defined_interface }]
         outside_targets: 10.249.29.149
         inside_sources:
            - 10.176.8.12/24
         inside_bind: [any named_interface {defined_interface} 10.299.10.12 ]
         ports:
            - 80/tcp
            - 443/tcp
       - outside_bind: [any named_interface { defined_interface }]
         outside_targets: 10.241.80.12
         inside_sources:
            - 10.0.8.12/24
         inside_bind: [any named_interface {defined_interface} ]
         ports:
            - 80/tcp
            - 443/tcp
            

  
         

  






