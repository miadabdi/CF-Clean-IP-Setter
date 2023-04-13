
import dns.resolver

def resolve_domains(domains):
    my_resolver = dns.resolver.Resolver(configure=False)
    my_resolver.nameservers = ['8.8.8.8', '1.1.1.1']

    ips = []
    for domain in domains:
        answer = my_resolver.query(domain)
        for rdata in answer:
            ips.append(str(rdata))

    print("Domains have been resolved")

    return ips