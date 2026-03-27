



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


![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/de3257b0-99da-4a97-9108-71d731170890/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663EKUVOMI%2F20260327%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260327T015616Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAcaCXVzLXdlc3QtMiJGMEQCIB0%2BIbQYaOeE9ISytFOSeJaMOQScT8NpxX87dZKv7XvAAiAQ6ncVDkmW6kcq0y607pLMIgGLawxA0eOguWEsSqc7tyqIBAjQ%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMXgB0BHElzww94TEyKtwDiVf2ljjkAS78NyOh1ef2%2F6Nl8vFBy2RP0CuwJzZKSL2%2F1xy0U5MWhIZMslNm3DfazX5GgHeAPPciJOj8FQO9unjWzRff0ikU3RBfx18LUPoa0QoDDkWcPGjx7C22OyYVFvfxJCUu0%2FCU%2FU8Xfzp0wk3sOCiM%2FQFskSHO9K08kiueCeMsoUEX8AaxY9YEcJhtFSH79t%2FZN8ogx62pqojTnSqFAZ9Va4rARn6YDcjYMKiX4F0RkPAAgiTD1zPftQcVL4%2F0gMexA3AZ1iyelcxfu9IQxwXKVOmWb1m77THEP0IzwmZsnJbZkC1rFjs4QJ5e2Nu1%2FrdNPbx543VGA8SWU76bSwYH3XmBLV3S%2FvboC2zlB3fqct4cm18%2BJ3R49unS4Ef4W0sNcC1aYUygoNLn%2FUz0dJC%2Bmn5J5%2BUurOMgTf9Gfp6Jjm%2BLeJm2qADNRctOeAjTlW7BzktRm0Qjj4YCETVuyKifelS2voTYeGYmVHFtA7sAdhk8OTOBCloiwJvskPar7%2FkbseAIq%2B2GO9xksTNpvGwlmTBFQyzmLTbWQvm7DFgrIFvX%2FL1DaEGIN%2BWEasUaQL4UdxDwIKCQwdK9ShVcaegxDMKPmDbVIaRhTDFvV1qxKDVqHwaT%2B60wgvGWzgY6pgHQrExgOeJQcybiMzJ9xdUdezvp2E45VeNahbUF%2BeVieehvaArP2qO4aLQ288H1DnK000lQshhswpv0sJCZ60gwYTwnS1ar%2FzGLL4bXSVoH6%2FyL8FgRWYWyR2aqNRemhvylK295bpmu8ePnG6vJnGf93ufkBuopqVdH%2FWDTCvFwE5TkTCSMo5rOFR4wQ4izsoGLNlBT%2BFqnzCMwUolCbENzigsYpwWr&X-Amz-Signature=ef67bdff470c4d22e54d0643e2e6a99474f1d9cee211d059323e54130c90d034&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



Port 443: HTTPS

HTTP method: GET



![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/dc56f68d-8daf-4b31-bc04-5bd2547ffac9/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663EKUVOMI%2F20260327%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260327T015617Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAcaCXVzLXdlc3QtMiJGMEQCIB0%2BIbQYaOeE9ISytFOSeJaMOQScT8NpxX87dZKv7XvAAiAQ6ncVDkmW6kcq0y607pLMIgGLawxA0eOguWEsSqc7tyqIBAjQ%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMXgB0BHElzww94TEyKtwDiVf2ljjkAS78NyOh1ef2%2F6Nl8vFBy2RP0CuwJzZKSL2%2F1xy0U5MWhIZMslNm3DfazX5GgHeAPPciJOj8FQO9unjWzRff0ikU3RBfx18LUPoa0QoDDkWcPGjx7C22OyYVFvfxJCUu0%2FCU%2FU8Xfzp0wk3sOCiM%2FQFskSHO9K08kiueCeMsoUEX8AaxY9YEcJhtFSH79t%2FZN8ogx62pqojTnSqFAZ9Va4rARn6YDcjYMKiX4F0RkPAAgiTD1zPftQcVL4%2F0gMexA3AZ1iyelcxfu9IQxwXKVOmWb1m77THEP0IzwmZsnJbZkC1rFjs4QJ5e2Nu1%2FrdNPbx543VGA8SWU76bSwYH3XmBLV3S%2FvboC2zlB3fqct4cm18%2BJ3R49unS4Ef4W0sNcC1aYUygoNLn%2FUz0dJC%2Bmn5J5%2BUurOMgTf9Gfp6Jjm%2BLeJm2qADNRctOeAjTlW7BzktRm0Qjj4YCETVuyKifelS2voTYeGYmVHFtA7sAdhk8OTOBCloiwJvskPar7%2FkbseAIq%2B2GO9xksTNpvGwlmTBFQyzmLTbWQvm7DFgrIFvX%2FL1DaEGIN%2BWEasUaQL4UdxDwIKCQwdK9ShVcaegxDMKPmDbVIaRhTDFvV1qxKDVqHwaT%2B60wgvGWzgY6pgHQrExgOeJQcybiMzJ9xdUdezvp2E45VeNahbUF%2BeVieehvaArP2qO4aLQ288H1DnK000lQshhswpv0sJCZ60gwYTwnS1ar%2FzGLL4bXSVoH6%2FyL8FgRWYWyR2aqNRemhvylK295bpmu8ePnG6vJnGf93ufkBuopqVdH%2FWDTCvFwE5TkTCSMo5rOFR4wQ4izsoGLNlBT%2BFqnzCMwUolCbENzigsYpwWr&X-Amz-Signature=1801d407dbeeb2f35e91dd39e0f6a9b3c26124fe4c726f9618303daacdad2174&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)





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







