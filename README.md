



ODATA —> Open Data Protocol 

                  (ISO International Organization for Standardization/

               IEC International Electrotechnical Commission approved)

    

    OASIS (Organization for the Advancement of Structured Information Standards) standard that defines a set of best practices for building and consuming RESTful APIs

     

## What is API?

    API (Application Programming Interface) is a set of rules, protocols, and tools that allows different software applications to communicate with each other.

## Four different ways API can work

    1. SOAP APIs:- XML, Used in past
    2. RPC APIs:- Remote Procedure Calls
    3. WebSocket APIs:- Used JSON objects, two way communication
    4. REST API: - Most Popular
    

# REST Principles/ 
architectural constraints

    

```mermaid

flowchart LR
  A[REST]
  A --> B[Uniform Interface]
  A --> C[Statelessness]
  A --> D[Client-Server]
  A --> E[Cacheabilit]
  A --> F[Layered System]
  A --> G[Code on Demand]
  
  style A fill:#64bef9, stroke:#000, stroke-width:2px,color:#000
  style B fill:#bce2fb, stroke:#000, stroke-width:2px,color:#000
  style A fill:#bce2fb, stroke:#000, stroke-width:2px,color:#000
  style C fill:#bce2fb, stroke:#000, stroke-width:2px,color:#000
  style D fill:#bce2fb, stroke:#000, stroke-width:2px,color:#000
  style E fill:#bce2fb, stroke:#000, stroke-width:2px,color:#000
  style F fill:#bce2fb, stroke:#000, stroke-width:2px,color:#000
  style G fill:#bce2fb, stroke:#000, stroke-width:2px,color:#000

```

## Uniform Interface

    It indicates Server transfers information in a standard format.

    5. The formatted resource is called a Representation in REST.
    6. Request should identify recourses by using URI
    7. Clients have enough information in the resource representation to modify, delete the resource. The server meets this condition by sending metadata that describes the resource further. 
    8. Client receive information about how to process the representation further. The server achieves this by sending self descriptive messages that contain metadata about how the client can best use them.
    9. For other related resourses server sends hyperlink in the represenation. So client can dynamically discover more resources.
    

## Statelessness

    

    10. Communication method in which the server completes every client request independently of all previous request.
## Layered System

    

    The client can connect to other authorized intermediaries between client and server.

## Catchability

    It stores some responses on the client or an intermediary to improve server response time.

## Code on Demand

    Server can temporarily extend or customize client functionality by transferring softare programming code to client

    Example:

    When you fill registration form on any websites, your browser heighlights mistake. Such as incorrect phone number. It can do this by the code sent by server. 

    

    

    



```mermaid
graph LR
  A[ODATA]--as --> B[Web SQL]
  style A fill:#0287de
  style B fill:#0287de
```





## Remote API vs Web API

Remote API: designed to interact with communication network. By remote, we mean that resources being manipulated by the API are somewhere outside computer making the request.



Web API: Communication Network(WWW)

ALL Web services are APIs, but not all APIs are web services.

## What does the RESTful API Client Request contain?

1. Unique recourse identifier:- URI ⇒ (URL- Location + URN-Name)
1. HTTP Method: GET, POST, DELETE, PUT, PATCH
1. HTTP Headers: Extra information


## What does the RESTful API server response contain?



- Status  line 
  1XX :- Informational → Processing 102

  2XX :- Success →Ok 200, Ok Created 201

  3XX :- Redirection → moved to new URL 301

  4XX :- Client Side Error → Bad request 400

  5XX:- Server Side Error → Not implemented 501



- Message body
  Contains recourse representation

-  Header


![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/de3257b0-99da-4a97-9108-71d731170890/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667ZPLYTMS%2F20260225%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260225T125415Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEUaCXVzLXdlc3QtMiJHMEUCIHk4wXGMA2ljhRtwAVlLUK%2BxRL73Xo5hyMW1Nmo%2FfSTFAiEAm4DAyz00TLTXaltZGi3qh16lOXHNCQfGyFjDm4EEorwq%2FwMIDhAAGgw2Mzc0MjMxODM4MDUiDJYHnlKPRPMC%2FbQLuyrcA0sK%2FSrWue2EHrNq4WoOuqJZrY9Xmex7PC3mz4JQmqigtr%2BdxEw5pnwpTyVgR1guLPw69NlevzRYyyRSRyxEDNDqlO0xHitvgDdBnrijjUXAZ83ub%2F%2BMBj%2BzZ%2FctGsnfredtXX4t5MEOUwx3VeTmBWNeooHpUuGZCrWzkl8QvZyWRMDq%2BT8ARbR8Uc5G1LvtTi0wBJ2DoWJh%2BBocCH1N6RK5I0e0v1Z%2BDFbODh%2BnL8IUMcGjqzeKU4juTAnsscJFsVgh1PxQosQO155q%2FQo1qjWFiwpqayM2n%2BiQiPF4tkRPz%2BCkH7AV8HZYpV6txMLdQCMlAlf88XdP3Ru784RAXC%2F3mdKfJfNqUSIXoprgD9RzG6rIYT48eOS4k7l9rsnjG3jF28wPJCVDqnKStXfMthv74tZmvjcSByUnyA0hY1BS4HrUEDTsP9X8STVu21lAMo41%2BmH%2FMD%2B3%2BaLjJHN3Xg9Aifp6hxNx%2BWsos%2FACQ%2FZV7rrMLgperd%2BbWjlCu9tQcDiKYDzk6a%2F09GSyI2ld6eHy%2FO4q3D2TYATEQFXzwS9HxE0%2FU3%2Fhvjmomof3JRhdjNAo3Uftq8V1od2ejVmV8tLFCS4SVku%2FcRWiRTU4HcIBI4IsTM%2Frmu%2Ftlc1YMLjf%2B8wGOqUBYiiM9Kw6y58QNINXjJsPDyzeNgUhI%2FfetVv%2Bljyo7LYzFBeKVR6nJ019P8hlXvjR244yCxDC2s%2Ffc8HFOWcX1DcEqHwgflAD0hWVnMGToa%2FatgtLUdNHRszlk1SqClH9D0jvIIStQulH4AQYvnGqxCtrC4qw367nLoX2%2FAnMN4YMfcMTT18ddA%2BYsfMvXy3eub0bd82wgA48KBwhwj8Kh1jPJUvH&X-Amz-Signature=afa4f033981dbc7271e92b82bac6cbbfd8735d4a812ff527a64163494bb3a847&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



Port 443: HTTPS

HTTP method: GET



![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/dc56f68d-8daf-4b31-bc04-5bd2547ffac9/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667ZPLYTMS%2F20260225%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260225T125416Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEUaCXVzLXdlc3QtMiJHMEUCIHk4wXGMA2ljhRtwAVlLUK%2BxRL73Xo5hyMW1Nmo%2FfSTFAiEAm4DAyz00TLTXaltZGi3qh16lOXHNCQfGyFjDm4EEorwq%2FwMIDhAAGgw2Mzc0MjMxODM4MDUiDJYHnlKPRPMC%2FbQLuyrcA0sK%2FSrWue2EHrNq4WoOuqJZrY9Xmex7PC3mz4JQmqigtr%2BdxEw5pnwpTyVgR1guLPw69NlevzRYyyRSRyxEDNDqlO0xHitvgDdBnrijjUXAZ83ub%2F%2BMBj%2BzZ%2FctGsnfredtXX4t5MEOUwx3VeTmBWNeooHpUuGZCrWzkl8QvZyWRMDq%2BT8ARbR8Uc5G1LvtTi0wBJ2DoWJh%2BBocCH1N6RK5I0e0v1Z%2BDFbODh%2BnL8IUMcGjqzeKU4juTAnsscJFsVgh1PxQosQO155q%2FQo1qjWFiwpqayM2n%2BiQiPF4tkRPz%2BCkH7AV8HZYpV6txMLdQCMlAlf88XdP3Ru784RAXC%2F3mdKfJfNqUSIXoprgD9RzG6rIYT48eOS4k7l9rsnjG3jF28wPJCVDqnKStXfMthv74tZmvjcSByUnyA0hY1BS4HrUEDTsP9X8STVu21lAMo41%2BmH%2FMD%2B3%2BaLjJHN3Xg9Aifp6hxNx%2BWsos%2FACQ%2FZV7rrMLgperd%2BbWjlCu9tQcDiKYDzk6a%2F09GSyI2ld6eHy%2FO4q3D2TYATEQFXzwS9HxE0%2FU3%2Fhvjmomof3JRhdjNAo3Uftq8V1od2ejVmV8tLFCS4SVku%2FcRWiRTU4HcIBI4IsTM%2Frmu%2Ftlc1YMLjf%2B8wGOqUBYiiM9Kw6y58QNINXjJsPDyzeNgUhI%2FfetVv%2Bljyo7LYzFBeKVR6nJ019P8hlXvjR244yCxDC2s%2Ffc8HFOWcX1DcEqHwgflAD0hWVnMGToa%2FatgtLUdNHRszlk1SqClH9D0jvIIStQulH4AQYvnGqxCtrC4qw367nLoX2%2FAnMN4YMfcMTT18ddA%2BYsfMvXy3eub0bd82wgA48KBwhwj8Kh1jPJUvH&X-Amz-Signature=deed9d6c5a498bef27d15f3fd2c8efcff16c5ebaf3911c32502f0c2745f29bea&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)





For HTTP PORT is 80



What is ODATA?

  ODATA is a Web protocol based om REST, for querying and updating Data.

Applying and building on Web technologies such as

  1. HTTP
  2. Atom publishing Protocol
  3. RSS ( Really Simple Syndication) 


Provide access information from Variety of applications.



## 

```mermaid
graph LR
  A[ODATA]
  A --> B[Format]
  A --> C[Protocol]
```

Format:- How data is described and how it is serialized.

Protocol:- How that Data is manipulated.



Origin of ODATA format





Final Test







