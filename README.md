



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


![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/de3257b0-99da-4a97-9108-71d731170890/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663DVWVBQN%2F20260110%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260110T062416Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEO7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIDOO234jJNCBdmMChVsV%2F7HnzlqajWJwEJm7UajtuDizAiEAmtMyG%2BBUuRuptstU8Wot1uunEKqBasO08T3X%2FFO6wggqiAQIt%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDHD6uS0COlNsoJMXYircA%2BVyGyUX6Kg1%2F1vuwMuJgoHfzXGEYhQWJUChH%2B6HA%2F22XvN2bYeQKhWSEoAORI%2BAIef1%2FWXJERhtfiGS3iClh6GaRncAOl318ABH3m7nwzKqC%2Bz9l3Xjofz14Dhxt2gHfzSwMi5oxn1Lo2Zlu5QxvP8bPTkfy5Se0%2FKg8pmAhju%2F%2BgR4cACQK2eY12405%2B5mlmIkjmwlzmvyNSRLf%2FYBEuBcmG6P5WmHNG8TdPLZQj2DBeWsH3DQAK9rN8FU6kUNHdei6pY2HabwC4MLqvq0qZjz4kyb67cdcclgZXOCgydkGaM22jCVeUepvgLQSivv4gNdxgOYz%2B3jz7vJqK0ixE9fOWd7zBnvx3EhbrDFcW%2BL%2B69nQ1HEnZDvby9SPpivh3uTWFuveNGJKAliBJ2P%2FFKMquw%2Bsi9JQbrXFPbensCErdS%2FnnhVVDVab6g4%2BmYuoZlVnG0Y%2BrwE5Ua1cq0ZDDEAPbydvEfWH6QvkmjUj8t9t%2BtQM5qST2zg7fGGRk4P%2FtXoTbq3hrp5h%2BUG8y4N3hr4vL3M5YiNz2v%2BsGXPDPfzXMlnYCbvXTKM851DSuO5uAjsHHpkuL2v3G%2FD9kBqnKHvYNUBUzgcy%2FMBk8jHD936Sg3QT4unETLvwrIFML3Vh8sGOqUBroOeRwj%2FIHk7JQnXWwgMnVf97Lr48%2BwNFVT3k8WyyX306nwryWx2zs4M6onKSvQb7Oyb3GHbEGXVhDW0Jaq19mnuYw%2FsTpDp4Wq79KqRPtmYnD5DQ8A6%2F4vM6eFFJbaMpKCcqX1Jd%2FiXwlDKCr373LUzE1daCC87qhYg0vDxDUK14JpmS%2BYklrRAqm30NOPhtle7nNNPwRhpx5lZbpAem4vqIPWX&X-Amz-Signature=7c91b1f8a30149581b1ea8f520e429e2ee71b4efa9a8e3db34f5d4ace46a4788&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



Port 443: HTTPS

HTTP method: GET



![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/dc56f68d-8daf-4b31-bc04-5bd2547ffac9/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663DVWVBQN%2F20260110%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260110T062416Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEO7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIDOO234jJNCBdmMChVsV%2F7HnzlqajWJwEJm7UajtuDizAiEAmtMyG%2BBUuRuptstU8Wot1uunEKqBasO08T3X%2FFO6wggqiAQIt%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDHD6uS0COlNsoJMXYircA%2BVyGyUX6Kg1%2F1vuwMuJgoHfzXGEYhQWJUChH%2B6HA%2F22XvN2bYeQKhWSEoAORI%2BAIef1%2FWXJERhtfiGS3iClh6GaRncAOl318ABH3m7nwzKqC%2Bz9l3Xjofz14Dhxt2gHfzSwMi5oxn1Lo2Zlu5QxvP8bPTkfy5Se0%2FKg8pmAhju%2F%2BgR4cACQK2eY12405%2B5mlmIkjmwlzmvyNSRLf%2FYBEuBcmG6P5WmHNG8TdPLZQj2DBeWsH3DQAK9rN8FU6kUNHdei6pY2HabwC4MLqvq0qZjz4kyb67cdcclgZXOCgydkGaM22jCVeUepvgLQSivv4gNdxgOYz%2B3jz7vJqK0ixE9fOWd7zBnvx3EhbrDFcW%2BL%2B69nQ1HEnZDvby9SPpivh3uTWFuveNGJKAliBJ2P%2FFKMquw%2Bsi9JQbrXFPbensCErdS%2FnnhVVDVab6g4%2BmYuoZlVnG0Y%2BrwE5Ua1cq0ZDDEAPbydvEfWH6QvkmjUj8t9t%2BtQM5qST2zg7fGGRk4P%2FtXoTbq3hrp5h%2BUG8y4N3hr4vL3M5YiNz2v%2BsGXPDPfzXMlnYCbvXTKM851DSuO5uAjsHHpkuL2v3G%2FD9kBqnKHvYNUBUzgcy%2FMBk8jHD936Sg3QT4unETLvwrIFML3Vh8sGOqUBroOeRwj%2FIHk7JQnXWwgMnVf97Lr48%2BwNFVT3k8WyyX306nwryWx2zs4M6onKSvQb7Oyb3GHbEGXVhDW0Jaq19mnuYw%2FsTpDp4Wq79KqRPtmYnD5DQ8A6%2F4vM6eFFJbaMpKCcqX1Jd%2FiXwlDKCr373LUzE1daCC87qhYg0vDxDUK14JpmS%2BYklrRAqm30NOPhtle7nNNPwRhpx5lZbpAem4vqIPWX&X-Amz-Signature=aff4a42342718f49fa0bd74b8eedb111ebf8eb2601b0ba7c37cfd0a587d7035b&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)





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







