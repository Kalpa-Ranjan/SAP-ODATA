



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


![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/de3257b0-99da-4a97-9108-71d731170890/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466577JSQW2%2F20251107%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251107T182130Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCxWT9OFT%2B5VoOKmmyyE0iNDdDlp%2Bjac%2FAb6iazBvVs3AIgL%2FCsguYg8kPxujizmpMwDtsNdxL8Pjqn4j1Y2wf68ckqiAQIw%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDJQhmdJAAj%2Bm6M4PcCrcA%2BelxuY2ngdrn8dJhkD5usBO%2BY8r58aJKnLZByRIOY0nL6o7bNxnbmIku1%2FpEUl3pe7vTrJoBlQWR4cA2PMSZj%2FPhRZZqFW0uFWnJEl6VAex6nCkPHHBJjAugvDeEKCQEXYNENpo9Nlc9HKsNno%2BGQmgs%2FvLFi7TMyHwrajARDif4I14oJUY3e5wSFo26meb6GpIBbJwA3hjr6yeqUI71bjTwRjE9HFYZzuApWCpEfQmNBqbf7w2yVb%2FsUCU7JpM7Xg2YMuuzMqYbYU2IOKvsNxgAHbo74qgteonPxH7Tzrzbpuqrc4ZIZalagV6hnQ8klyOn6S1I0Gw43tqKtJhcjWbsC%2BB%2BFXR1ke3idbK7N2fKS1M7rnCEFwvN4EvfHYWVcxtLpcWO%2BqdJj5ELDoAkQeS0lzwFe%2BjotlKNiDJ7SPwqeX13BkgLVcKPd2GA3q5sUOgANiFKJszrp0knbouNvpGqTEl5txPVxK3MF928mK9t%2BZl6uLZlDseMUvKeEhTCP2rH2cigMg0shZ8eXjuWJbGJxIr8AQU9mK9yggLq1fsgxbbJe5WfMJzJaMos7rO5YMGzRDGYUo8hgSg9UH41%2FBPj6yFdYo21ns1pqDhngA0kxplW5cBkZFoFwXmMIzYuMgGOqUBlrUECStAsbdFJcJUQ7NZ44PYdrXDawDGQJKqNMZvDXuQrcRnt95us8%2BCTlmttfr0jqc%2FukHhINWP2BUiXz5zKY0wfAYpUxOQOtyRUEaZX1BocvvQ0i2%2BtoUUl2NcwkMd7eKrqlCl4JGw2lV7kNLxD1%2B1QWJSStC57w2xX4faSaYqBF%2BqFA%2BZ7Z7JVu5KYWSjSLiRBeXuNtAg%2F1IQOTeNiOMdsmm3&X-Amz-Signature=567abce9f5e43cbdc1c72d1d43e104eaf1a3374206a51a1ba1f1b0086f96ea87&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



Port 443: HTTPS

HTTP method: GET



![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/dc56f68d-8daf-4b31-bc04-5bd2547ffac9/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466577JSQW2%2F20251107%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251107T182130Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCxWT9OFT%2B5VoOKmmyyE0iNDdDlp%2Bjac%2FAb6iazBvVs3AIgL%2FCsguYg8kPxujizmpMwDtsNdxL8Pjqn4j1Y2wf68ckqiAQIw%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDJQhmdJAAj%2Bm6M4PcCrcA%2BelxuY2ngdrn8dJhkD5usBO%2BY8r58aJKnLZByRIOY0nL6o7bNxnbmIku1%2FpEUl3pe7vTrJoBlQWR4cA2PMSZj%2FPhRZZqFW0uFWnJEl6VAex6nCkPHHBJjAugvDeEKCQEXYNENpo9Nlc9HKsNno%2BGQmgs%2FvLFi7TMyHwrajARDif4I14oJUY3e5wSFo26meb6GpIBbJwA3hjr6yeqUI71bjTwRjE9HFYZzuApWCpEfQmNBqbf7w2yVb%2FsUCU7JpM7Xg2YMuuzMqYbYU2IOKvsNxgAHbo74qgteonPxH7Tzrzbpuqrc4ZIZalagV6hnQ8klyOn6S1I0Gw43tqKtJhcjWbsC%2BB%2BFXR1ke3idbK7N2fKS1M7rnCEFwvN4EvfHYWVcxtLpcWO%2BqdJj5ELDoAkQeS0lzwFe%2BjotlKNiDJ7SPwqeX13BkgLVcKPd2GA3q5sUOgANiFKJszrp0knbouNvpGqTEl5txPVxK3MF928mK9t%2BZl6uLZlDseMUvKeEhTCP2rH2cigMg0shZ8eXjuWJbGJxIr8AQU9mK9yggLq1fsgxbbJe5WfMJzJaMos7rO5YMGzRDGYUo8hgSg9UH41%2FBPj6yFdYo21ns1pqDhngA0kxplW5cBkZFoFwXmMIzYuMgGOqUBlrUECStAsbdFJcJUQ7NZ44PYdrXDawDGQJKqNMZvDXuQrcRnt95us8%2BCTlmttfr0jqc%2FukHhINWP2BUiXz5zKY0wfAYpUxOQOtyRUEaZX1BocvvQ0i2%2BtoUUl2NcwkMd7eKrqlCl4JGw2lV7kNLxD1%2B1QWJSStC57w2xX4faSaYqBF%2BqFA%2BZ7Z7JVu5KYWSjSLiRBeXuNtAg%2F1IQOTeNiOMdsmm3&X-Amz-Signature=c52b92b46cd5578d18575f063288c69ec421e4abf335e75896e38a01b31fd7cb&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)





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







