



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


![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/de3257b0-99da-4a97-9108-71d731170890/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WSC37YC5%2F20251223%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251223T123434Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEQaCXVzLXdlc3QtMiJHMEUCIQDDE3rOR0SbOUW2M3GUH5H6QOX5PRQgLKfm6JacF5UhxQIgarws3UXX3ZgArmmS62YJ7LDperuX%2BYMaC2vrYtw%2Be2Uq%2FwMIDRAAGgw2Mzc0MjMxODM4MDUiDEiCh7J8BA013c%2FsCircA0WQMM89NfEB8XMBl6rPAeoCMcxXt%2B%2F%2BRam3LWGpxjsyMEL6Txf8GRVFpiJlHTWfWUI%2Fg07RFmf5YrcrDCmNIAWgHDOX2HU2oQgujf9K95sSFAMkJQufkNDyJTtncQnbGpgQ7V9AGb5qPxD08pja13%2FhFrZlbMLIWjfMgFVKr%2Ba7AATatA5VqRFGh0G3GJijZpeH68McrAtvWLtn7DhQyTeetrI9sPSPjVoRhFjDrdbs8QFzcF7rywGbINcAjcqfwdD7RqXRZKmY%2BF6hI4K%2FWlAz%2FeC1jVW7FDjoFkne19BGk0C%2Fz8%2FROpPQM7bD3kl4Bla%2BAdTo5d4r5yWuKGIdJi6YKPUdRT4Hl%2FHfEKzZw7DcfZWbrZ2hIvdtm1DgtFttrkp0hZXm1dw6u6xYRG1Yg1Eiy2ngoHu2IAKfXbZdyNTOppdTaiAs%2Bb9V317wmR0Vv5Gek0ZPswIhQs6hX1rjE4xTth8e2npIThGCX12yIR5jJ%2BVRKdHF7Xg6BMVqbvzTBmRYhNCYwyJQqWPTVCMbpUg267wanpg5gME7CLcLrRQDwSw%2F4SfKFAy71lYRzc1erHqwYNw649UJ0jAMzV4fWkRKLB0rt6R9eRbdNf%2FLFyM4bUpUtTBFjJVXtX3QMNiBqsoGOqUBrRnRLieF6q8awU04pY2L2is491GGx9eznu29nEY1ryLeYBtSZrtFfYwDAopDplcTHdYUEFpBK%2BVTrxBtck2kIiQ6vfkAH3Qtz3m4c8D%2Fa9s4AmBa%2FzfMuVlDlN4dUABcqBk99QGLTBK0p7URoWWVm3eb6f%2F64De8pw621HbuYM6qJCUn%2BUPVGhHgvWRgeCcIH35ujg0kRT1WVtkYyfki%2FYyEOtel&X-Amz-Signature=9fa1a75e351c99ab82e35c1e0921c98a99a280d1e53c4eb1c96181b5639c4cc0&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



Port 443: HTTPS

HTTP method: GET



![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/dc56f68d-8daf-4b31-bc04-5bd2547ffac9/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WSC37YC5%2F20251223%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251223T123434Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEQaCXVzLXdlc3QtMiJHMEUCIQDDE3rOR0SbOUW2M3GUH5H6QOX5PRQgLKfm6JacF5UhxQIgarws3UXX3ZgArmmS62YJ7LDperuX%2BYMaC2vrYtw%2Be2Uq%2FwMIDRAAGgw2Mzc0MjMxODM4MDUiDEiCh7J8BA013c%2FsCircA0WQMM89NfEB8XMBl6rPAeoCMcxXt%2B%2F%2BRam3LWGpxjsyMEL6Txf8GRVFpiJlHTWfWUI%2Fg07RFmf5YrcrDCmNIAWgHDOX2HU2oQgujf9K95sSFAMkJQufkNDyJTtncQnbGpgQ7V9AGb5qPxD08pja13%2FhFrZlbMLIWjfMgFVKr%2Ba7AATatA5VqRFGh0G3GJijZpeH68McrAtvWLtn7DhQyTeetrI9sPSPjVoRhFjDrdbs8QFzcF7rywGbINcAjcqfwdD7RqXRZKmY%2BF6hI4K%2FWlAz%2FeC1jVW7FDjoFkne19BGk0C%2Fz8%2FROpPQM7bD3kl4Bla%2BAdTo5d4r5yWuKGIdJi6YKPUdRT4Hl%2FHfEKzZw7DcfZWbrZ2hIvdtm1DgtFttrkp0hZXm1dw6u6xYRG1Yg1Eiy2ngoHu2IAKfXbZdyNTOppdTaiAs%2Bb9V317wmR0Vv5Gek0ZPswIhQs6hX1rjE4xTth8e2npIThGCX12yIR5jJ%2BVRKdHF7Xg6BMVqbvzTBmRYhNCYwyJQqWPTVCMbpUg267wanpg5gME7CLcLrRQDwSw%2F4SfKFAy71lYRzc1erHqwYNw649UJ0jAMzV4fWkRKLB0rt6R9eRbdNf%2FLFyM4bUpUtTBFjJVXtX3QMNiBqsoGOqUBrRnRLieF6q8awU04pY2L2is491GGx9eznu29nEY1ryLeYBtSZrtFfYwDAopDplcTHdYUEFpBK%2BVTrxBtck2kIiQ6vfkAH3Qtz3m4c8D%2Fa9s4AmBa%2FzfMuVlDlN4dUABcqBk99QGLTBK0p7URoWWVm3eb6f%2F64De8pw621HbuYM6qJCUn%2BUPVGhHgvWRgeCcIH35ujg0kRT1WVtkYyfki%2FYyEOtel&X-Amz-Signature=fcecf31dc917bbe1adfc1396022d30f782fd193b4b11921dc11bba8d8cf32106&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)





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







