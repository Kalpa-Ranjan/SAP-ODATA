



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


![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/de3257b0-99da-4a97-9108-71d731170890/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466Z3L3E3FI%2F20260505%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260505T191151Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEML%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIG1zEN0%2BTOpAN1PuA1sdeXQlLGsFOf0bvwMbNyl%2BNaZRAiEA3zac9CCoDKmbAkm%2BzKRZsfIcIXWclAB8J7dI0fFhAZUqiAQIi%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDIuyQQYXmFAdW250vyrcA%2FsxzPtgolwFWSRgoUsggQKY9cu5hbd3kBEN5MJMS7ymmI2LoenEgsEDa300gOv8lWnwsBC7XV%2BcOq%2B%2Bx9v%2FpY0A3sKBQIGduScDJB9rUMmcUiujKkLObuGVlMHN%2FsoAwqqI%2FsM28uqfMLYzhOJCBo2lYhJoGnrfgJ82UBHae%2BOYDCRzU7X3fiulT%2BP8Oj8JwGRxB%2BKdJ6Vbaeb8OowWy3OH6RiCWhhHI7sI%2BjN%2BZv4DmzaSYxdYgPX%2BJt00hvTJg7c2O%2Fn2XOIejuvcmv3P7T5OPDD%2BUgI5bLJv058JoCY6g7aIINjx2A%2BgGRl8gGfrUJcA9iV%2FXBGYLQniJGN7KIVfd3vkNHmrHtzemfr45Up3FD8TLFgW6ltc3Mhs4PEahMlTSUgauFzJFjQucemtLFOUg2MZtLNcyBOzkmUv8hTd3sacJSycfLnfCkZagTjm5s2drnogWX3D6f0VsB2BlbNy9UEWWVTLxjP%2Bz7o5C%2FjJ%2BQLyLGbAZ5dJsgbaB5GUsJhP0cdI6A26ome05K5OixfyenVW6g%2F5oq9PxwwCvM43X1Dwk8fi3BPTIKrSpKZbAXWea3zywAR051z75gGxprhY%2BtYxKEs39YJQuLKOeTILp1sMgGK3c80CyeQnMKno6M8GOqUBwHWi9wjjeBQtmh6SPb1lp2xklZ8YYTf%2FjGQZ%2B924di4DTuYFc0vQAMxfp9EnROJB7JocKCJkCxP9i3SpCS2J0iS4IeBg%2Bst14LV6ZgFUtQGzHvlnVHUqFKW%2F0MbSc6QU8lizccYFDUzYmwDlnuhZyvBPAqqvoNVor1PcsQSRPGT%2BxaczdDoDPStQ5NXHbwp8lwZhQKPXkdLmid%2FO4tjT3J55x4Si&X-Amz-Signature=b11603708d0470b2197f3c56ee623febfe458ccb171edc44eb6458b5574dda13&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



Port 443: HTTPS

HTTP method: GET



![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/dc56f68d-8daf-4b31-bc04-5bd2547ffac9/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466Z3L3E3FI%2F20260505%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260505T191151Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEML%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIG1zEN0%2BTOpAN1PuA1sdeXQlLGsFOf0bvwMbNyl%2BNaZRAiEA3zac9CCoDKmbAkm%2BzKRZsfIcIXWclAB8J7dI0fFhAZUqiAQIi%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDIuyQQYXmFAdW250vyrcA%2FsxzPtgolwFWSRgoUsggQKY9cu5hbd3kBEN5MJMS7ymmI2LoenEgsEDa300gOv8lWnwsBC7XV%2BcOq%2B%2Bx9v%2FpY0A3sKBQIGduScDJB9rUMmcUiujKkLObuGVlMHN%2FsoAwqqI%2FsM28uqfMLYzhOJCBo2lYhJoGnrfgJ82UBHae%2BOYDCRzU7X3fiulT%2BP8Oj8JwGRxB%2BKdJ6Vbaeb8OowWy3OH6RiCWhhHI7sI%2BjN%2BZv4DmzaSYxdYgPX%2BJt00hvTJg7c2O%2Fn2XOIejuvcmv3P7T5OPDD%2BUgI5bLJv058JoCY6g7aIINjx2A%2BgGRl8gGfrUJcA9iV%2FXBGYLQniJGN7KIVfd3vkNHmrHtzemfr45Up3FD8TLFgW6ltc3Mhs4PEahMlTSUgauFzJFjQucemtLFOUg2MZtLNcyBOzkmUv8hTd3sacJSycfLnfCkZagTjm5s2drnogWX3D6f0VsB2BlbNy9UEWWVTLxjP%2Bz7o5C%2FjJ%2BQLyLGbAZ5dJsgbaB5GUsJhP0cdI6A26ome05K5OixfyenVW6g%2F5oq9PxwwCvM43X1Dwk8fi3BPTIKrSpKZbAXWea3zywAR051z75gGxprhY%2BtYxKEs39YJQuLKOeTILp1sMgGK3c80CyeQnMKno6M8GOqUBwHWi9wjjeBQtmh6SPb1lp2xklZ8YYTf%2FjGQZ%2B924di4DTuYFc0vQAMxfp9EnROJB7JocKCJkCxP9i3SpCS2J0iS4IeBg%2Bst14LV6ZgFUtQGzHvlnVHUqFKW%2F0MbSc6QU8lizccYFDUzYmwDlnuhZyvBPAqqvoNVor1PcsQSRPGT%2BxaczdDoDPStQ5NXHbwp8lwZhQKPXkdLmid%2FO4tjT3J55x4Si&X-Amz-Signature=ae6bee6299570bd6bceb1bea9ed2fd44d7b8f484a1ab5540c37b7133561d53a2&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)





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







