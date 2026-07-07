



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


![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/de3257b0-99da-4a97-9108-71d731170890/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YDWCJ4PV%2F20260707%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260707T023653Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCYrxI748jNt6mro9fnayXfU59Pq19i4sPKgDeZWjCvQAIgIEcPoWjknEB2NawKymIJFX4Wbyroynv1V248O2XisB0q%2FwMIYxAAGgw2Mzc0MjMxODM4MDUiDO70yyOY9mi%2Bmv%2FvCyrcA2WKQLVn28rW0XZ%2FKvpjMWNBvWkAThesRNJtwQfb3wD6OkhRGqNzsWCQlCjVHYSpY7Y1cyFkbXLELFvOosVi5vW62Xbf9ADepIMpYM9eSk8OBj6AnIA5gwpn%2BhX5ps1wiJ5Kob4mZVwpoqez00FRq3Xd9IuEPoJ6wmauprqpxyLSP%2F4XgMRZ5krLWJww2zRwHFyzzvZvo2KCB%2F8ad7w4kofsI%2FjQxZSZuULna24e6Xin7XLUKWlT%2FQZDDhAJ%2BlMsfC9DlivBenQN%2BY4jWsjv8ik5B3jo%2BhdowePUiUZjzuR3YA18rURzUw9KxTsdPN90EWQCL1jUvnlkd4MaBQ75WrYMaX6wjlZeIXuqmPj3L3VBx8ka2A6cJot%2Bd2OasDPiifejoGut9mctm%2BRZb7nPviM3f9lzV3kO88Q6V80saVMIzNPFRBqy2tSavI80YojhYHZ1zD52haBjtmtnNnqQSqNSBl9i2l84Gv7RQfbTKXHWZDeKT%2BGrMCWCmnky2cgq1rvNGylbInfR2KsJbYBjjdO7p0IXQlm1yAIZWVDBcIrnjJUP2wBs7AqzFnOA49T8NIP%2BvQJwhZHNjzPXFs6nRsYcGERiuG7v%2FmOvLb2PdckOJ84dDnWmX%2FTBlIuLMITAsdIGOqUBHZuxUildai5KMYyv%2BMHn49qOYUa8LL4yVeMVNWsEVY141dWh79gmVHkVgMd0FnJG3oIeb1UXxdJM6WChdYe98jfs7nf7iY5EZV9Zx90ZKIHEpukabBjPTwHI8Xm5GW1U%2FuvuOMJLKzjK4qRl5847SJDo8w%2BFK2KVgCA99lWochs%2FAL%2B5IgUpWNVWyvHRcjQGas87%2BBcDMdV2KD1V0X1ebcjee3ey&X-Amz-Signature=fc4fe14c5a4b1c4f04771fd61019d91bb4a137eb5facc3565d6d1fdc20d379ed&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



Port 443: HTTPS

HTTP method: GET



![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/dc56f68d-8daf-4b31-bc04-5bd2547ffac9/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YDWCJ4PV%2F20260707%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260707T023653Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCYrxI748jNt6mro9fnayXfU59Pq19i4sPKgDeZWjCvQAIgIEcPoWjknEB2NawKymIJFX4Wbyroynv1V248O2XisB0q%2FwMIYxAAGgw2Mzc0MjMxODM4MDUiDO70yyOY9mi%2Bmv%2FvCyrcA2WKQLVn28rW0XZ%2FKvpjMWNBvWkAThesRNJtwQfb3wD6OkhRGqNzsWCQlCjVHYSpY7Y1cyFkbXLELFvOosVi5vW62Xbf9ADepIMpYM9eSk8OBj6AnIA5gwpn%2BhX5ps1wiJ5Kob4mZVwpoqez00FRq3Xd9IuEPoJ6wmauprqpxyLSP%2F4XgMRZ5krLWJww2zRwHFyzzvZvo2KCB%2F8ad7w4kofsI%2FjQxZSZuULna24e6Xin7XLUKWlT%2FQZDDhAJ%2BlMsfC9DlivBenQN%2BY4jWsjv8ik5B3jo%2BhdowePUiUZjzuR3YA18rURzUw9KxTsdPN90EWQCL1jUvnlkd4MaBQ75WrYMaX6wjlZeIXuqmPj3L3VBx8ka2A6cJot%2Bd2OasDPiifejoGut9mctm%2BRZb7nPviM3f9lzV3kO88Q6V80saVMIzNPFRBqy2tSavI80YojhYHZ1zD52haBjtmtnNnqQSqNSBl9i2l84Gv7RQfbTKXHWZDeKT%2BGrMCWCmnky2cgq1rvNGylbInfR2KsJbYBjjdO7p0IXQlm1yAIZWVDBcIrnjJUP2wBs7AqzFnOA49T8NIP%2BvQJwhZHNjzPXFs6nRsYcGERiuG7v%2FmOvLb2PdckOJ84dDnWmX%2FTBlIuLMITAsdIGOqUBHZuxUildai5KMYyv%2BMHn49qOYUa8LL4yVeMVNWsEVY141dWh79gmVHkVgMd0FnJG3oIeb1UXxdJM6WChdYe98jfs7nf7iY5EZV9Zx90ZKIHEpukabBjPTwHI8Xm5GW1U%2FuvuOMJLKzjK4qRl5847SJDo8w%2BFK2KVgCA99lWochs%2FAL%2B5IgUpWNVWyvHRcjQGas87%2BBcDMdV2KD1V0X1ebcjee3ey&X-Amz-Signature=2302908c75a8e35353425797a9217626b12ecedbe837afc090122621e928a6eb&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)





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







