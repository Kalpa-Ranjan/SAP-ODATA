



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


![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/de3257b0-99da-4a97-9108-71d731170890/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667U7ZAAIP%2F20260709%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260709T144540Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENX%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIHQHV%2FjkTTeC7%2FmmIjt3jUlQ4B3VzuUePuq0z61PXFFqAiEAtvez2jXzfWu9s4tfvNBNIsdtg%2FHCGn0iw3VwOnJkEv0qiAQInv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDA650AWokE4%2BhZvKKyrcA3M0jDEC%2F9pmL0tfqRSepHsAydUaj8yMURxitxIndV8L3u7qTM2vJnp2ol7BNks4hzfLkOLOzOKwx1kHJ%2FQ6i8nYGwv%2B1mEUVhXUZZ1kmJ6Viz%2FPN%2FJDWGU5fHKgOXjk5Mr4XUPJkCSkOxSmn40tp2UTiXMEtoP8GyrZVrdwzG9C0OIWHhs7xqUqCMZe8j4z8Y6zuO6oQAc1Xfp3AvoWmGA74KfgUGhTwtXsbYNIiv1pES5gsYsw%2FbpxHUy%2FkWGZSI5yjDyXYuFtzMHzKNCx5L%2F9WSqQhjGiUSW1J5AsURpGOo1cnL049kyb7MXUPPEnVIo7TsoYZWf2FJQCHw9x370RPg7J80l6m%2BEKPbhYY0fZJGy25dU7%2F5ksUKZAjZjYkzoLWgL%2BfjaesU6kngKixD2XkrPwsUINLm1QKWsASjsn3cTg%2BR%2FChDxqXGYzIAIBMScfMTGp3xtnZFgeLeIlni4dfhbxIDRFkfQ6I4pJoCN4th2LKlcvUh2MQvopMzodLs26d7%2B%2BhAuP5WwAMTYyc%2F5VvkDV63dZ3Uai9lXjN%2Frp08VWl7%2F4xCInF17nDjmJ9%2BHYWVglu%2BxScuxjIrgbDaKpQNpdtK6Z%2B5robVdZEw2iWKBJiqPV66hS9j76MJq7vtIGOqUBOCQCSFBiCNfz%2Be4s7qD6b8MqFkuWE7bayCOd2%2FaVC10S3wRtwuodKSVks%2BFKpPzkUGRAY9Zh%2Fcud8cPMR4uSiAsml1xAD89AIQmA5uVySMyZVBWZdqr8d%2BhamWJ6l768A%2F74Gv6%2BBTDm93ENWcQaNK%2BjzrQaRfqIXQqgncVS32KLPLEtgiyng64D18UT5ddmeu6opDpihF5aLrQHePnVD936SOBf&X-Amz-Signature=54ad560802d59c25d38ac9d39b76b9f18f0145a47f5c91dec0a7801a0b8f5774&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



Port 443: HTTPS

HTTP method: GET



![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/dc56f68d-8daf-4b31-bc04-5bd2547ffac9/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667U7ZAAIP%2F20260709%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260709T144540Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENX%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIHQHV%2FjkTTeC7%2FmmIjt3jUlQ4B3VzuUePuq0z61PXFFqAiEAtvez2jXzfWu9s4tfvNBNIsdtg%2FHCGn0iw3VwOnJkEv0qiAQInv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDA650AWokE4%2BhZvKKyrcA3M0jDEC%2F9pmL0tfqRSepHsAydUaj8yMURxitxIndV8L3u7qTM2vJnp2ol7BNks4hzfLkOLOzOKwx1kHJ%2FQ6i8nYGwv%2B1mEUVhXUZZ1kmJ6Viz%2FPN%2FJDWGU5fHKgOXjk5Mr4XUPJkCSkOxSmn40tp2UTiXMEtoP8GyrZVrdwzG9C0OIWHhs7xqUqCMZe8j4z8Y6zuO6oQAc1Xfp3AvoWmGA74KfgUGhTwtXsbYNIiv1pES5gsYsw%2FbpxHUy%2FkWGZSI5yjDyXYuFtzMHzKNCx5L%2F9WSqQhjGiUSW1J5AsURpGOo1cnL049kyb7MXUPPEnVIo7TsoYZWf2FJQCHw9x370RPg7J80l6m%2BEKPbhYY0fZJGy25dU7%2F5ksUKZAjZjYkzoLWgL%2BfjaesU6kngKixD2XkrPwsUINLm1QKWsASjsn3cTg%2BR%2FChDxqXGYzIAIBMScfMTGp3xtnZFgeLeIlni4dfhbxIDRFkfQ6I4pJoCN4th2LKlcvUh2MQvopMzodLs26d7%2B%2BhAuP5WwAMTYyc%2F5VvkDV63dZ3Uai9lXjN%2Frp08VWl7%2F4xCInF17nDjmJ9%2BHYWVglu%2BxScuxjIrgbDaKpQNpdtK6Z%2B5robVdZEw2iWKBJiqPV66hS9j76MJq7vtIGOqUBOCQCSFBiCNfz%2Be4s7qD6b8MqFkuWE7bayCOd2%2FaVC10S3wRtwuodKSVks%2BFKpPzkUGRAY9Zh%2Fcud8cPMR4uSiAsml1xAD89AIQmA5uVySMyZVBWZdqr8d%2BhamWJ6l768A%2F74Gv6%2BBTDm93ENWcQaNK%2BjzrQaRfqIXQqgncVS32KLPLEtgiyng64D18UT5ddmeu6opDpihF5aLrQHePnVD936SOBf&X-Amz-Signature=714751d02ceae1507b8e0741e70feeab8de3635e0b6969d64636dd00e13a13f4&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)





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







