



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


![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/de3257b0-99da-4a97-9108-71d731170890/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666CDR5EQ4%2F20261024%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20261024T061134Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDY8wPMBI5tAAkEE5AQXcnSNdKEKO8FZvmu3RfSbCawYQIgZ4l8C5Ei8%2Bi3HPwB8HrQuRItIS2G3Fre%2FhtrZKzXnfcqiAQInv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDAkgEZzAgr6FQ5iygircAxodY38HCZM0doaA1gALjZJvphFSUq%2FLIYifavAjM%2Ba0F%2BwZw7mPlNeD8dW3ekMNwx6c69QQMZJuCqaSmscG24FlRlyvAw930XPd6pQSyP5%2B1ob2WEJWjS4DC9ghOaYwt2Qe0DWttrkZLX1BCY2tEG7QRmg8kSRDCeyg%2FzxEb6USI4sJdbsQVVEHKzJ59VIvH%2FPS1FcLonIe1qlxbPGEOOKPT9KA0BThH23KxJlJlv4yAGVa9vr5e9ATrvs%2BBzPa66ND3%2Ba8tK5sjkXC6RK4tu0bCreX7DPNfsf5OsO7TRyexztgKjsVPbH2MVPOL8k1dKhWR42UcxqVkfea7FPl3Q9VTG3Uba%2FZ6RK%2BFT%2B2ZMQij92an6s9ILuHgAyIZ751JzSx67kNlmSX6l3exsPoBfN5c1tqQLzKoKDj%2F5qQtLpXyQ5sbOJFeZ%2FPXZMAdNp6uQQG7EorWhkKs3J%2F8uZkPhLFlp3bPsyiP7tPt4vuA45Ju89f7tVr5Cx4yZzP1SbsleG5OYU%2FyKelXTdJGffxpvsFbojTd9fXcX05Jdyfw%2FCad9TmZpzUsuicFD1JbfCJTX3f5VJTVssd2vnVlKVK5%2BWmiJF9c2dli073AmKNFEP%2FKahaZkDnfTwkmvk6MMaE8dYGOqUBGMmx6yUXJjK3v3weIycW8EuY%2Bt13IDz7lJH%2BBCXl2JVbZIq6Dg6wpzO%2F62R1UvZYE%2FB8iMTtqqGjCsTQpctc9Iv76OxvfcPd5yauOjAaRegrUarKfdbN0uxGu%2BopobuPWFE0dSWM3wo5%2Bv1TZykYC3hnBI%2BQwSmKDm8dFSXgE%2Bx3MQDDk9qIKwMM02fi6NfwyrCvZf5l1xLlZ%2FgErq7vSpneMcOG&X-Amz-Signature=57caeff575a3fa7eb3bab319f95c7b3b01a8b76621d07791e31e81629e5c7074&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



Port 443: HTTPS

HTTP method: GET



![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/dc56f68d-8daf-4b31-bc04-5bd2547ffac9/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666CDR5EQ4%2F20261024%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20261024T061134Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDY8wPMBI5tAAkEE5AQXcnSNdKEKO8FZvmu3RfSbCawYQIgZ4l8C5Ei8%2Bi3HPwB8HrQuRItIS2G3Fre%2FhtrZKzXnfcqiAQInv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDAkgEZzAgr6FQ5iygircAxodY38HCZM0doaA1gALjZJvphFSUq%2FLIYifavAjM%2Ba0F%2BwZw7mPlNeD8dW3ekMNwx6c69QQMZJuCqaSmscG24FlRlyvAw930XPd6pQSyP5%2B1ob2WEJWjS4DC9ghOaYwt2Qe0DWttrkZLX1BCY2tEG7QRmg8kSRDCeyg%2FzxEb6USI4sJdbsQVVEHKzJ59VIvH%2FPS1FcLonIe1qlxbPGEOOKPT9KA0BThH23KxJlJlv4yAGVa9vr5e9ATrvs%2BBzPa66ND3%2Ba8tK5sjkXC6RK4tu0bCreX7DPNfsf5OsO7TRyexztgKjsVPbH2MVPOL8k1dKhWR42UcxqVkfea7FPl3Q9VTG3Uba%2FZ6RK%2BFT%2B2ZMQij92an6s9ILuHgAyIZ751JzSx67kNlmSX6l3exsPoBfN5c1tqQLzKoKDj%2F5qQtLpXyQ5sbOJFeZ%2FPXZMAdNp6uQQG7EorWhkKs3J%2F8uZkPhLFlp3bPsyiP7tPt4vuA45Ju89f7tVr5Cx4yZzP1SbsleG5OYU%2FyKelXTdJGffxpvsFbojTd9fXcX05Jdyfw%2FCad9TmZpzUsuicFD1JbfCJTX3f5VJTVssd2vnVlKVK5%2BWmiJF9c2dli073AmKNFEP%2FKahaZkDnfTwkmvk6MMaE8dYGOqUBGMmx6yUXJjK3v3weIycW8EuY%2Bt13IDz7lJH%2BBCXl2JVbZIq6Dg6wpzO%2F62R1UvZYE%2FB8iMTtqqGjCsTQpctc9Iv76OxvfcPd5yauOjAaRegrUarKfdbN0uxGu%2BopobuPWFE0dSWM3wo5%2Bv1TZykYC3hnBI%2BQwSmKDm8dFSXgE%2Bx3MQDDk9qIKwMM02fi6NfwyrCvZf5l1xLlZ%2FgErq7vSpneMcOG&X-Amz-Signature=25c812ce204b859d819b650cb2d501c324ede3cdeff37632827bc3e1b9adba8b&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)





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







