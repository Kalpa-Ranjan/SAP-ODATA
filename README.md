



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


![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/de3257b0-99da-4a97-9108-71d731170890/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665WABAX7D%2F20260217%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260217T014613Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHkaCXVzLXdlc3QtMiJIMEYCIQCh30SkkXdQX%2BXT3oGRmrcz8k1NREwGyXBDNtntgk094gIhAOzTvHpTAT0duPMZJMuH0DGmNhopKXyHgUmk11eZLg9XKv8DCEIQABoMNjM3NDIzMTgzODA1Igz2W6W0I7m43VtBS%2Fwq3ANkl7pzSqMLzViaBzZDYhP9H3aNa7umKz9%2F%2Bvxw0cnHDmZX2AqMoi0VyCT2ID5ErOCFl1Ll0%2FnxPXEPBSSCzVxKvg%2FjY53KCmN5AQrdUwoh56tGnjededLkkXwEQYBhHLArU%2Fmrp1X3fUnTrzi8z50x7rOlvXGmO0hAhQEknG%2BPhJaZczRo5DnhFIWiPoW4mizsJWFSTVrOR4iMGg%2FOPoQckEKCAmWgr%2FTfkcbOWmmMmVGrdfJyYENDXpEeQN8W5SyGS1%2FU0%2FoNsiOdvduKnUzkptU%2Fn6sdFo87OrADhV5aQIYxcnoVLWkM1FIIfGXAHLlMkelang%2Fm531zregT9vL914p4NfJQ%2FuLphWB7fQybG6XTPhDoaRbXeGiDojnhgD8i7dg2h8TfMjl8KHsCMNLQ%2F%2Fvikind2WRnN%2BmaQFXlDBfxm%2FiemJ8Tsftx7Hmm%2FYrar%2B74VMMwl4G9nsmjhMpZNmL9bMkZn8cSl4P%2FzX3GJYYdEQL6XIQrtMOTgH0TLbq%2Bwfk7W90nOb2OON6ULWVtuZ7v5WY1XD1bxq9hz4J2QytIP8kB7OzcYaAVLK%2F3Y%2FG9ug3ShFpQtzb%2Ft4WAFRzsk9sW93nSyOCZNW3OIyt%2F8tF1RCiA9wQJyfi2GTDl8M7MBjqkAcY3dcIvSwYmdQTrx8cSUxUqlb6NxZAyOWdC1BJt0uk3PSpg%2B5EJPuOdtYQUolcPJfx%2Bh45KGVzv7KfDGVxtscgSvxcpWyKtqn9bjeFw4Gz8VLTRoc3w7%2FPmCF0ChACFCNfGw%2F8nICuyo%2BUCvNFZeDcdkCzA3%2FqqfpDg45JqlONkpHnGc27mW7hBmDY6L1Gpv1yPTa%2FQNkDOiWtIJcT8ePR1oqK3&X-Amz-Signature=59ae9b37628feb59c9aa5eb244f3bc8fa9c9a7c075c4b347928aa29d1bd2ffea&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



Port 443: HTTPS

HTTP method: GET



![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/dc56f68d-8daf-4b31-bc04-5bd2547ffac9/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665WABAX7D%2F20260217%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260217T014613Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHkaCXVzLXdlc3QtMiJIMEYCIQCh30SkkXdQX%2BXT3oGRmrcz8k1NREwGyXBDNtntgk094gIhAOzTvHpTAT0duPMZJMuH0DGmNhopKXyHgUmk11eZLg9XKv8DCEIQABoMNjM3NDIzMTgzODA1Igz2W6W0I7m43VtBS%2Fwq3ANkl7pzSqMLzViaBzZDYhP9H3aNa7umKz9%2F%2Bvxw0cnHDmZX2AqMoi0VyCT2ID5ErOCFl1Ll0%2FnxPXEPBSSCzVxKvg%2FjY53KCmN5AQrdUwoh56tGnjededLkkXwEQYBhHLArU%2Fmrp1X3fUnTrzi8z50x7rOlvXGmO0hAhQEknG%2BPhJaZczRo5DnhFIWiPoW4mizsJWFSTVrOR4iMGg%2FOPoQckEKCAmWgr%2FTfkcbOWmmMmVGrdfJyYENDXpEeQN8W5SyGS1%2FU0%2FoNsiOdvduKnUzkptU%2Fn6sdFo87OrADhV5aQIYxcnoVLWkM1FIIfGXAHLlMkelang%2Fm531zregT9vL914p4NfJQ%2FuLphWB7fQybG6XTPhDoaRbXeGiDojnhgD8i7dg2h8TfMjl8KHsCMNLQ%2F%2Fvikind2WRnN%2BmaQFXlDBfxm%2FiemJ8Tsftx7Hmm%2FYrar%2B74VMMwl4G9nsmjhMpZNmL9bMkZn8cSl4P%2FzX3GJYYdEQL6XIQrtMOTgH0TLbq%2Bwfk7W90nOb2OON6ULWVtuZ7v5WY1XD1bxq9hz4J2QytIP8kB7OzcYaAVLK%2F3Y%2FG9ug3ShFpQtzb%2Ft4WAFRzsk9sW93nSyOCZNW3OIyt%2F8tF1RCiA9wQJyfi2GTDl8M7MBjqkAcY3dcIvSwYmdQTrx8cSUxUqlb6NxZAyOWdC1BJt0uk3PSpg%2B5EJPuOdtYQUolcPJfx%2Bh45KGVzv7KfDGVxtscgSvxcpWyKtqn9bjeFw4Gz8VLTRoc3w7%2FPmCF0ChACFCNfGw%2F8nICuyo%2BUCvNFZeDcdkCzA3%2FqqfpDg45JqlONkpHnGc27mW7hBmDY6L1Gpv1yPTa%2FQNkDOiWtIJcT8ePR1oqK3&X-Amz-Signature=e8b3b37eb8c10bd24f11e110ab1af628ed3c4ad7ef1ed04ac5a51c6957c63944&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)





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







