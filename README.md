



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


![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/de3257b0-99da-4a97-9108-71d731170890/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665AK6JGHT%2F20260614%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260614T135049Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHgaCXVzLXdlc3QtMiJIMEYCIQD1gyDkhEvmG%2BUA1A6YNikpVEy21%2BHpBBXS%2BsmMr0JelQIhAI5CSN7EEQ2SoclMezbnM07K1ow9d22kkzAHNG6ViEJpKv8DCEEQABoMNjM3NDIzMTgzODA1IgwKWXM%2F7J5F%2BEUurMoq3AOQ05%2Bl4ELW3gykSAfMHMBiAuRq7HWaFj8Xw9EN6Y8qdn13MAPk7QNe%2FotYc8dr0HE4WkQ7k9Uy8maphK4BXoJ1ogoaARIxag%2FKaOaiYNRlyd8octz6GZexmfY3ptw6VKbf1ss%2BZrQDnUgLAflJ2wA60IP6hHlK4CgvWfs5vYFsTkuiEEO0F1BpZVKVH1WSzLktIUslZVh59%2FcqjwUuqoI9QSrb0KJPbq8%2FLQoYqva%2FPT3qUh3Yez7SVd%2BI75ZFDpGYvBYdvEsZEb2e8vJ2nbNsJIJGYgvxFEnCPEcdWlbeeMHO5cIc5P%2FHP3cHnU%2FrQS0QtBuCJffrbQbp4I07rTh6R9Y%2BHsdP3zG7Er7q25SDdIXeJTSbg3%2FZRlcDHfvdIRwbTN1chjLgrip7dGDbZnTvwOX%2BTJpg4JZ9o4EXqyR8uHbj%2FcffNF28Fspx0iP7SrsHmqtgPd8acvPHpvkrcjDuzDC%2BZVR%2Fh99Hj%2BE8Np4zli3LEO7HJdT8exWLgsaOTmch%2FB7hr0cVK93zvp6ebEKjKBI3B9g7Q%2B08owRXQwl%2F%2FGvjIR2QaCHim60AI39AzVVWX4JrZNiPOR7CWtLQK7mf4P3KXXmJXRpoxq5kMTJFFxsbMRMAL7eKgQRAxzCZx7nRBjqkAX8f6adUO0%2FrYgV5Xebc%2FxJfarFzS5eKakJBiWYwU2QNkvUOWnBLl%2BkTHopQnHezw3KrxY6KRQdGQ9R8fquImmPab8vqyHWNEawAxvgMOdr8qJJwlbmx52rALvrh99KaWnFMzW1MLprg3eGUkDlzKi41XBgNlEqHLPiuBzTI9ic7ANfFp0q6OeBqpQJawRfDiHhUE9BIpqreDc0MhkQJ27UNJxEl&X-Amz-Signature=208d8cfee9086f783e6a5686688433264a2052fbe6cdd0de3fb946fff7bd4951&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



Port 443: HTTPS

HTTP method: GET



![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/dc56f68d-8daf-4b31-bc04-5bd2547ffac9/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665AK6JGHT%2F20260614%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260614T135049Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHgaCXVzLXdlc3QtMiJIMEYCIQD1gyDkhEvmG%2BUA1A6YNikpVEy21%2BHpBBXS%2BsmMr0JelQIhAI5CSN7EEQ2SoclMezbnM07K1ow9d22kkzAHNG6ViEJpKv8DCEEQABoMNjM3NDIzMTgzODA1IgwKWXM%2F7J5F%2BEUurMoq3AOQ05%2Bl4ELW3gykSAfMHMBiAuRq7HWaFj8Xw9EN6Y8qdn13MAPk7QNe%2FotYc8dr0HE4WkQ7k9Uy8maphK4BXoJ1ogoaARIxag%2FKaOaiYNRlyd8octz6GZexmfY3ptw6VKbf1ss%2BZrQDnUgLAflJ2wA60IP6hHlK4CgvWfs5vYFsTkuiEEO0F1BpZVKVH1WSzLktIUslZVh59%2FcqjwUuqoI9QSrb0KJPbq8%2FLQoYqva%2FPT3qUh3Yez7SVd%2BI75ZFDpGYvBYdvEsZEb2e8vJ2nbNsJIJGYgvxFEnCPEcdWlbeeMHO5cIc5P%2FHP3cHnU%2FrQS0QtBuCJffrbQbp4I07rTh6R9Y%2BHsdP3zG7Er7q25SDdIXeJTSbg3%2FZRlcDHfvdIRwbTN1chjLgrip7dGDbZnTvwOX%2BTJpg4JZ9o4EXqyR8uHbj%2FcffNF28Fspx0iP7SrsHmqtgPd8acvPHpvkrcjDuzDC%2BZVR%2Fh99Hj%2BE8Np4zli3LEO7HJdT8exWLgsaOTmch%2FB7hr0cVK93zvp6ebEKjKBI3B9g7Q%2B08owRXQwl%2F%2FGvjIR2QaCHim60AI39AzVVWX4JrZNiPOR7CWtLQK7mf4P3KXXmJXRpoxq5kMTJFFxsbMRMAL7eKgQRAxzCZx7nRBjqkAX8f6adUO0%2FrYgV5Xebc%2FxJfarFzS5eKakJBiWYwU2QNkvUOWnBLl%2BkTHopQnHezw3KrxY6KRQdGQ9R8fquImmPab8vqyHWNEawAxvgMOdr8qJJwlbmx52rALvrh99KaWnFMzW1MLprg3eGUkDlzKi41XBgNlEqHLPiuBzTI9ic7ANfFp0q6OeBqpQJawRfDiHhUE9BIpqreDc0MhkQJ27UNJxEl&X-Amz-Signature=845a670f8b2b4624b45107e434e727df4a510bd6c5c4db3363c4aae78bcadcdc&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)





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







