



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


![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/de3257b0-99da-4a97-9108-71d731170890/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WCPMNI3V%2F20260305%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260305T125049Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAQaCXVzLXdlc3QtMiJGMEQCIHqfr09XGe8PN2UdZtJiwT3JI9%2F9e3YcKgStcHJAGbCuAiAG0YaYsjJAz3JQFgke%2BfdoT80A0buny%2BEPKeAKDpuBcyqIBAjN%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMGJo9uaYvi1R%2FS4asKtwDTVd1PYW7%2BwjrZ9C2s2ilakTv%2Bjyv0c%2B%2BWzAyzhGY6SqidnCQrkC5uw1iu6MRra0iieqnSgzY4Tk96BxdwAx7htyLu9tfDyN56d31bbBDOmX5ZeVg9OC2F3gwnCnNxmKPrD7UsNVjIhtOiy0sXC5aHdXVdFQCThv6%2BpZts598YyUtlCh8058y6kDgcRwCk14c4fyD%2BDlhNTAeORLOCOHGXqvOhPiz7NmBgKskSYGfctW5LZsvNCxFp5wxjUkzEr36YiVvH9qub5h5txx0v99cbdxft%2FPFN36WV%2Bt8beWhiZ14KUTOeYFGwwvKGXsfaamlD2C2E7tk46T0qJbGNeev5SSxuX7O6Dzg0aN7OBPV%2FfJaZDqUZT9VmWalZvcchr%2F07BscmDGXOQt6ZTuQGyBcVy98C36It0SsF3TDxDsx1BmCdmsSl9t%2FlvZ0snGq6GUqORI9SRRGBSsttcEDWwyUuxkoWS3Ek%2BOyuY7YeDTuYwqTbMgoItIibk0ZhhzchEVtnOvTkBzzw75PGodS6KHhDjaLvCxrXjRBMNRSmgF9XyajVjnkqxtnDsn84oq%2BJc%2Bk8M4QsLnuuCrquF0fFPOjtKzj0uOhYEU28j9N9b%2BVXMlcBAcP0Bg8cjWMDTkw4dGlzQY6pgEa0tuy9pl6V7h%2BEf%2F%2FyzXDwBc4kx8bqU8MyPy4kpmmUqTX4wDi9TS0O5c%2BQuT06rRDnAtLRYHq%2Fv1dqzS7pjIcaGVx3lKi7GhFxknuxeQS%2F7mpJ5e9lPRjlBIyY4EeVBOck8qk%2FhOHjrN02dNRlaBzF0U12T49kQAIP%2B05OOk3E0oTkk8sNwCckuqF9zgmJj4og9sDhyMiwwx%2B6JOQtr2dBJIUa7t5&X-Amz-Signature=725a139462f8018e3a5bddbd4ece175edc808b152fd827932fc3efd0497bc29d&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



Port 443: HTTPS

HTTP method: GET



![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/dc56f68d-8daf-4b31-bc04-5bd2547ffac9/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WCPMNI3V%2F20260305%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260305T125050Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAQaCXVzLXdlc3QtMiJGMEQCIHqfr09XGe8PN2UdZtJiwT3JI9%2F9e3YcKgStcHJAGbCuAiAG0YaYsjJAz3JQFgke%2BfdoT80A0buny%2BEPKeAKDpuBcyqIBAjN%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMGJo9uaYvi1R%2FS4asKtwDTVd1PYW7%2BwjrZ9C2s2ilakTv%2Bjyv0c%2B%2BWzAyzhGY6SqidnCQrkC5uw1iu6MRra0iieqnSgzY4Tk96BxdwAx7htyLu9tfDyN56d31bbBDOmX5ZeVg9OC2F3gwnCnNxmKPrD7UsNVjIhtOiy0sXC5aHdXVdFQCThv6%2BpZts598YyUtlCh8058y6kDgcRwCk14c4fyD%2BDlhNTAeORLOCOHGXqvOhPiz7NmBgKskSYGfctW5LZsvNCxFp5wxjUkzEr36YiVvH9qub5h5txx0v99cbdxft%2FPFN36WV%2Bt8beWhiZ14KUTOeYFGwwvKGXsfaamlD2C2E7tk46T0qJbGNeev5SSxuX7O6Dzg0aN7OBPV%2FfJaZDqUZT9VmWalZvcchr%2F07BscmDGXOQt6ZTuQGyBcVy98C36It0SsF3TDxDsx1BmCdmsSl9t%2FlvZ0snGq6GUqORI9SRRGBSsttcEDWwyUuxkoWS3Ek%2BOyuY7YeDTuYwqTbMgoItIibk0ZhhzchEVtnOvTkBzzw75PGodS6KHhDjaLvCxrXjRBMNRSmgF9XyajVjnkqxtnDsn84oq%2BJc%2Bk8M4QsLnuuCrquF0fFPOjtKzj0uOhYEU28j9N9b%2BVXMlcBAcP0Bg8cjWMDTkw4dGlzQY6pgEa0tuy9pl6V7h%2BEf%2F%2FyzXDwBc4kx8bqU8MyPy4kpmmUqTX4wDi9TS0O5c%2BQuT06rRDnAtLRYHq%2Fv1dqzS7pjIcaGVx3lKi7GhFxknuxeQS%2F7mpJ5e9lPRjlBIyY4EeVBOck8qk%2FhOHjrN02dNRlaBzF0U12T49kQAIP%2B05OOk3E0oTkk8sNwCckuqF9zgmJj4og9sDhyMiwwx%2B6JOQtr2dBJIUa7t5&X-Amz-Signature=34854cddf61b215b44b03aeeb09832a421c4da257b0d6fb058d0c163677b16ea&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)





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







