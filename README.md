



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


![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/de3257b0-99da-4a97-9108-71d731170890/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466X3MTVZBU%2F20260831%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260831T122819Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIBrq%2B%2FPXIlNlmg4lyA2G6KzcD4Zp%2FEuAP1VMvwGs8kUAAiEAuvY2LzqUhbSxuF56p7MI%2FVxkvVNOqomVBZEUfjT8bqQqiAQIlP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDEcLvkgIg3NTaEiVfyrcA64TF5EFS1qzoJgA%2FaAut4d3iOaQEQq6vCnLUZwLj9R4RG3wvY9FvUoXWPcYOKCkqX70p%2FA7iJRbikKa5jEtoWuU5y2T2fb0mD4oqeLBtXh5O6d7Ul8huM1Yia7V24JNOR5ZA605Rn%2FSScoPeB66yIYtcmaT9ca4jfdemynXbSVlH%2BN0t8IfK7ej28RDWbmZ2b3QATOrjG%2FfdQYy0rJvQeW50qhaPe%2BskOAe9z3U46XAATHhXgnYLqnHG6%2BMHyR2aIA78M44EiYXsV9reBvVE9JBcgwq44sS4ZcVYSmCwYBoQq3xrucdw3Q6l1SUkc%2F0vsnh5tONggNFQvy%2BRQxwtvv3KqNMQzaPSAGTi%2Bg9RRZC1QdDfHFzV05Pvb8TuqRWoCGKRdVyOuCA1tRN%2BlNr8GuCicGzr2e90XBUi2eUsDyKDiwAOegskLGwVPjTQwH5syhwbfel%2BiGqpQhzVubnfgjikgu%2FqQ5VXNeMqKeCIpvPS32zJx5F39syfHo24z1cTLG2dtDqDrmDPp2qsRKuO2oliWjUi%2BZ7kesFy9RlpqiFDb1TJFkyVOVa0uqZMugknWfr5WKdqzl9mAA9sqP06RNzDS8Y24%2Bf2124guPP0oTsUnqbTWQJhA98AOnGMOS51dQGOqUBCpS0u9G1hbBruHTrAX79Ll%2BI%2FrNBvk4jB7WnWQwQv4bbYjPl7YJoaoD0jI%2B%2FEkzWpOIpO5xmVzmboLRNpVcKplpU2Fgfs4oUi%2FNIkshO3DS%2FZbQHEnCSIjnBYcayGZje2vgBgQaSbfymzEde6r65sjOIBvEQS%2BuEw932fgSNfiFGYTMoeeEUTkgp0W1rIDf%2FIahKmOhjbwgZqZoDNZrK5IBBj%2Fvj&X-Amz-Signature=6d053e5c2ad4de94c7a9d60150f30dc77d479799b64fb944d3bae02b1fda3e04&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



Port 443: HTTPS

HTTP method: GET



![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/dc56f68d-8daf-4b31-bc04-5bd2547ffac9/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466X3MTVZBU%2F20260831%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260831T122819Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIBrq%2B%2FPXIlNlmg4lyA2G6KzcD4Zp%2FEuAP1VMvwGs8kUAAiEAuvY2LzqUhbSxuF56p7MI%2FVxkvVNOqomVBZEUfjT8bqQqiAQIlP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDEcLvkgIg3NTaEiVfyrcA64TF5EFS1qzoJgA%2FaAut4d3iOaQEQq6vCnLUZwLj9R4RG3wvY9FvUoXWPcYOKCkqX70p%2FA7iJRbikKa5jEtoWuU5y2T2fb0mD4oqeLBtXh5O6d7Ul8huM1Yia7V24JNOR5ZA605Rn%2FSScoPeB66yIYtcmaT9ca4jfdemynXbSVlH%2BN0t8IfK7ej28RDWbmZ2b3QATOrjG%2FfdQYy0rJvQeW50qhaPe%2BskOAe9z3U46XAATHhXgnYLqnHG6%2BMHyR2aIA78M44EiYXsV9reBvVE9JBcgwq44sS4ZcVYSmCwYBoQq3xrucdw3Q6l1SUkc%2F0vsnh5tONggNFQvy%2BRQxwtvv3KqNMQzaPSAGTi%2Bg9RRZC1QdDfHFzV05Pvb8TuqRWoCGKRdVyOuCA1tRN%2BlNr8GuCicGzr2e90XBUi2eUsDyKDiwAOegskLGwVPjTQwH5syhwbfel%2BiGqpQhzVubnfgjikgu%2FqQ5VXNeMqKeCIpvPS32zJx5F39syfHo24z1cTLG2dtDqDrmDPp2qsRKuO2oliWjUi%2BZ7kesFy9RlpqiFDb1TJFkyVOVa0uqZMugknWfr5WKdqzl9mAA9sqP06RNzDS8Y24%2Bf2124guPP0oTsUnqbTWQJhA98AOnGMOS51dQGOqUBCpS0u9G1hbBruHTrAX79Ll%2BI%2FrNBvk4jB7WnWQwQv4bbYjPl7YJoaoD0jI%2B%2FEkzWpOIpO5xmVzmboLRNpVcKplpU2Fgfs4oUi%2FNIkshO3DS%2FZbQHEnCSIjnBYcayGZje2vgBgQaSbfymzEde6r65sjOIBvEQS%2BuEw932fgSNfiFGYTMoeeEUTkgp0W1rIDf%2FIahKmOhjbwgZqZoDNZrK5IBBj%2Fvj&X-Amz-Signature=1ba6fb7f2ea0ba7c2c460d0a9b874f6eebad2449234fa2b187b4f68638d14c5b&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)





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







