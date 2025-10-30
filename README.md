



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


![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/de3257b0-99da-4a97-9108-71d731170890/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666HWQMCGP%2F20251030%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251030T230956Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjED4aCXVzLXdlc3QtMiJIMEYCIQDlnQ9ePtSoyYO3z4OSePcA%2Fic5wWuDFH01LfRBNJfI3QIhAJWku4kqRYnRl6mjyn3FV6dRbYKJHa6lMpiBPP6dRjc9KogECPf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igyvdd6C1nNZ%2Bzn0InIq3AMyViZrr%2Fa0%2Bbme%2Fg3lDzQ5YuXHkZeGrgDqNNMqhfxDkHOHhjjXre9lJgDM7aMCvHeu3VdoNhleG8c93p5RWmIv5q5OhjQqHOLS5ESp4vS1m9v5Hbs1%2BE1a8WJyfuuYMZsSb9QxbQrvbv11UOZU2ZumgNS7%2B2sN9Dn8VN%2BkNIegMZLx8tMK3GtgCUsQChmsYLgRjukPuHQNibkYQUoN5UYj6TMRgs%2BmJszrpo3SPeqTF64WOMSdl%2FBIZzfKCtE8PO0Hm1nT3hf8we3zuHGJeR4VpgUdRAZAq4NPQsmZBhqV8uzLxijvFtDE6K2Z8pJDzriMI9x6RE7MsX4kI73mtO41%2BAb%2FYV%2FrtLefgBsJcqIUw6P5BU6rda8aW0wTPR1Imqnngm56TkZmL9%2B3tFjjUx3rxq%2BS1OB%2B6tze1JujPSfqlP5xTBv5rdjFo0MPPHW1A7UZmh5t7fbgVaSz1UJ%2BbIov9Jj6%2BGOFdsoSaeY43AUT%2FHUiWBIuyO2E8GNwbGZfAqXpZcMNryvVSvzfDEiSbGtMAMPLZWGPw9DNqt%2FAwx9TiodyGgEWFIxzu4j3uOQPBCD2GDZTuihufVmn2PzUsC4VLIrgkEVP83xSlEdX5wJWLri9tNVoWiHvj5ihEjCTxo%2FIBjqkAX%2FkeMzn2Y5btWHnicTzgAYUAljceDpIcNJhJSimqoQ1ww11ZJAYrCaoN99EqIoXOUNBx0i%2BXUdcnhIOSsovQLiRHxwCIh0pF8ciG5lfYvSG9h85xur5TsnGcbBftSvAcRtYUozirBw3r91Uoio6AhXtTnXWT96ir97JSRuutRo760N6Yi%2Bk%2FUvID%2Fysx4w1ogDd4mY%2BiNIztlMdT8PRlbpaRmso&X-Amz-Signature=abb8ab51d59d2ddb3c9126fb77165fb2d86c6f1848729317db5da08098fb72bf&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



Port 443: HTTPS

HTTP method: GET



![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/dc56f68d-8daf-4b31-bc04-5bd2547ffac9/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666HWQMCGP%2F20251030%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251030T230956Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjED4aCXVzLXdlc3QtMiJIMEYCIQDlnQ9ePtSoyYO3z4OSePcA%2Fic5wWuDFH01LfRBNJfI3QIhAJWku4kqRYnRl6mjyn3FV6dRbYKJHa6lMpiBPP6dRjc9KogECPf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igyvdd6C1nNZ%2Bzn0InIq3AMyViZrr%2Fa0%2Bbme%2Fg3lDzQ5YuXHkZeGrgDqNNMqhfxDkHOHhjjXre9lJgDM7aMCvHeu3VdoNhleG8c93p5RWmIv5q5OhjQqHOLS5ESp4vS1m9v5Hbs1%2BE1a8WJyfuuYMZsSb9QxbQrvbv11UOZU2ZumgNS7%2B2sN9Dn8VN%2BkNIegMZLx8tMK3GtgCUsQChmsYLgRjukPuHQNibkYQUoN5UYj6TMRgs%2BmJszrpo3SPeqTF64WOMSdl%2FBIZzfKCtE8PO0Hm1nT3hf8we3zuHGJeR4VpgUdRAZAq4NPQsmZBhqV8uzLxijvFtDE6K2Z8pJDzriMI9x6RE7MsX4kI73mtO41%2BAb%2FYV%2FrtLefgBsJcqIUw6P5BU6rda8aW0wTPR1Imqnngm56TkZmL9%2B3tFjjUx3rxq%2BS1OB%2B6tze1JujPSfqlP5xTBv5rdjFo0MPPHW1A7UZmh5t7fbgVaSz1UJ%2BbIov9Jj6%2BGOFdsoSaeY43AUT%2FHUiWBIuyO2E8GNwbGZfAqXpZcMNryvVSvzfDEiSbGtMAMPLZWGPw9DNqt%2FAwx9TiodyGgEWFIxzu4j3uOQPBCD2GDZTuihufVmn2PzUsC4VLIrgkEVP83xSlEdX5wJWLri9tNVoWiHvj5ihEjCTxo%2FIBjqkAX%2FkeMzn2Y5btWHnicTzgAYUAljceDpIcNJhJSimqoQ1ww11ZJAYrCaoN99EqIoXOUNBx0i%2BXUdcnhIOSsovQLiRHxwCIh0pF8ciG5lfYvSG9h85xur5TsnGcbBftSvAcRtYUozirBw3r91Uoio6AhXtTnXWT96ir97JSRuutRo760N6Yi%2Bk%2FUvID%2Fysx4w1ogDd4mY%2BiNIztlMdT8PRlbpaRmso&X-Amz-Signature=b7a33412b00a1b7d1833fbf82f8255fd9680a0c31a6e023dcd80971dfa9cbe44&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)





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







