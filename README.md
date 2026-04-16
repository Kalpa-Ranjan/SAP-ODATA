



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


![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/de3257b0-99da-4a97-9108-71d731170890/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662SSK3TWD%2F20260416%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260416T020925Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDG1jfPwHu%2FASR6lMIrjPxsCptdg3Xl3G2Nxe5uW7xV0wIgYPQEzIIxG%2BZhOq8gIHKFzY7wUDFmAhL2mBSCG9%2BIk1wqiAQIs%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDJRR%2FW4LRJsbuTtaQCrcA7bxpWWs2fQ99aOaKCNn1po1v%2Fs4Cgt7%2BCijNSVWpB%2FUDlxJl9dbhxcmCr7EMHRxM%2BYJqICLtx54JwJZ68VjGvikV3Hs5QzR08oLjibUmzjN30qlJQB4rfMn9e5336GjWBaZLY3ChcVkpyBWCdVq8XE48nRdZtB%2B3fc2I%2BcV35Kq7m4ztdx2wqMGn9nkbsivsjEtoEQNEo1ZCmExS3HXx7dwZAXVWdp9BZQCzv7uQU40UvL2t0%2FNAYv7b%2BOcZzUAPBOYTh0TJpTt9YDuVlJdCUJA2cm8ieX9HBMrf9tRGdKCLJzCuKAIxg27mqGe%2Fvb7lnnVv0HUGQxiWb74E60fIf7sraASKCF0vZwefvwEZM%2FKi2w1WfVtii2wNRSdKhAF93LUrRaf%2Bwx5PuLbEDnoKc7TRDtXNhUGtzx5g2EBZt4bl5i%2FIfRxrujhV0csbRLjJ5wI0SldQk%2FsdKrqS0At1AMnzKYBtlHyDNIeM9K0kYE0T6L16ejvr%2FeWP6BP5K6s5zjC6g0JJ7N5jWo5RlWVaJFHGV9hckQ%2FUS2qPJktFuCIf9Y%2Faorp3LGTWj%2F1IEEsGG6166RyoK8LE%2FNUm%2B8YKQMcNCtlAdmUD06nkix9RBwDqKOqLufm2tyc9VsRMM%2BHgc8GOqUBEFYGv7UDoeKkOyJl0foKBvhx495DDM4FiDE6Ct1rhZgBV7kWBwJFzXfK4etDCMvTWpXclMtRBCeqB5TCRZIOGWa60Wn5XrrSJnyeOj7gzOUlzqe3T1%2B3mn1fzAEGVIAgRhgwwnQVF%2FDP794SJUfw%2F5x6Y3dwuBo2V%2Fs110HzQKugY207vcaBnWuex%2BIN80XUS12rjfuPv1EzqSJOzZYr2tZrv2%2Bc&X-Amz-Signature=1eef23fb494db545acd07d1f119e9e20f8739f5a9435185ab1e01ce9598dc519&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



Port 443: HTTPS

HTTP method: GET



![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/dc56f68d-8daf-4b31-bc04-5bd2547ffac9/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662SSK3TWD%2F20260416%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260416T020925Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDG1jfPwHu%2FASR6lMIrjPxsCptdg3Xl3G2Nxe5uW7xV0wIgYPQEzIIxG%2BZhOq8gIHKFzY7wUDFmAhL2mBSCG9%2BIk1wqiAQIs%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDJRR%2FW4LRJsbuTtaQCrcA7bxpWWs2fQ99aOaKCNn1po1v%2Fs4Cgt7%2BCijNSVWpB%2FUDlxJl9dbhxcmCr7EMHRxM%2BYJqICLtx54JwJZ68VjGvikV3Hs5QzR08oLjibUmzjN30qlJQB4rfMn9e5336GjWBaZLY3ChcVkpyBWCdVq8XE48nRdZtB%2B3fc2I%2BcV35Kq7m4ztdx2wqMGn9nkbsivsjEtoEQNEo1ZCmExS3HXx7dwZAXVWdp9BZQCzv7uQU40UvL2t0%2FNAYv7b%2BOcZzUAPBOYTh0TJpTt9YDuVlJdCUJA2cm8ieX9HBMrf9tRGdKCLJzCuKAIxg27mqGe%2Fvb7lnnVv0HUGQxiWb74E60fIf7sraASKCF0vZwefvwEZM%2FKi2w1WfVtii2wNRSdKhAF93LUrRaf%2Bwx5PuLbEDnoKc7TRDtXNhUGtzx5g2EBZt4bl5i%2FIfRxrujhV0csbRLjJ5wI0SldQk%2FsdKrqS0At1AMnzKYBtlHyDNIeM9K0kYE0T6L16ejvr%2FeWP6BP5K6s5zjC6g0JJ7N5jWo5RlWVaJFHGV9hckQ%2FUS2qPJktFuCIf9Y%2Faorp3LGTWj%2F1IEEsGG6166RyoK8LE%2FNUm%2B8YKQMcNCtlAdmUD06nkix9RBwDqKOqLufm2tyc9VsRMM%2BHgc8GOqUBEFYGv7UDoeKkOyJl0foKBvhx495DDM4FiDE6Ct1rhZgBV7kWBwJFzXfK4etDCMvTWpXclMtRBCeqB5TCRZIOGWa60Wn5XrrSJnyeOj7gzOUlzqe3T1%2B3mn1fzAEGVIAgRhgwwnQVF%2FDP794SJUfw%2F5x6Y3dwuBo2V%2Fs110HzQKugY207vcaBnWuex%2BIN80XUS12rjfuPv1EzqSJOzZYr2tZrv2%2Bc&X-Amz-Signature=9aa2c9d15b058cc55584c31988abed58451f6c182a3f2450885c7a72d06ac847&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)





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







