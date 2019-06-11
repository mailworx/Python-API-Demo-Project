from zeep import Client

client = Client('http://localhost:55824/services/serviceagent.asmx?WSDL')

factory = client.type_factory('ns0')
securityContext = factory.SecurityContext(Username="[Username]", Password="[Password]", Account="[Account]", Source="[Source]")

field = factory.TextField(InternalName="email", UntypedValue="[email]", Guid="00000000-0000-0000-0000-000000000000")
fields = factory.ArrayOfField(Field=[field])

subscriber = factory.Subscriber(Language="DE", Guid="00000000-0000-0000-0000-000000000000", Status="Active", SmsStatus="Active", Mailformat="Multipart", DOIStatus="DocumentedExternally", Fields=fields)
subscribers = factory.ArrayOfSubscriber(Subscriber=[subscriber])
print(subscribers)

importRequest = factory.SubscriberImportRequest(SecurityContext=securityContext, Subscribers=subscribers, DuplicateCriteria="email", Language="DE")
response = client.service.ImportSubscribers(importRequest)

print(response)