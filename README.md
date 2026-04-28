



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


![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/de3257b0-99da-4a97-9108-71d731170890/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466US7POWYB%2F20260428%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260428T081529Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBAaCXVzLXdlc3QtMiJHMEUCIQC%2FgtcQlwliQGejGV%2BKfRDFqrqfOzGo4%2BXJtRq0CwmckgIgb092wDGYVrX%2F819CJBhMKLb3WxAh2vFmK%2Bh8v%2BwXzF0qiAQI2f%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDM7VqUb0RAK%2BXgn98yrcAzuQ24qlkqYtQVTMyondgGDDZv7C39WkYfZO1jlBIJWP2%2BVFo4l%2BiBmts33M5md5XJ4rnpIqp%2FAkghiQmtkaGNIbaHX6Ycgr50OModf16Y0EsSMIpefqKSy5Bn9WFeR3gZGVO84lU%2BPiQjqlOTUoS8nJ7tgGMzmjYPv8CZXJtg7R6vvumTqPXWVTNVDJg0IHY73QM2dBQqbuylC5CDLj4OwossJmzNtWclYVKYgTMLwhoYpFrlx7hnI%2FtTLP6bLXnbvehSVZexdxgadCMmFSyf8YigKnSZT%2BWMx1hkZyob%2B6NL4o8ovL3RhT2l7TdAgA63BGxKZJzasQt%2BleID8Z%2FULg2BGGI8zps%2FEQcw0nmI3dyLKfD94s%2FG3kbhX7XUytyhp370I01RA%2FH6jaLkkqs3eGaoVvef7wB19FXXxSio0rs109t5rA5MVeTOC46MX1OqdF1JoO2nh5uqxnHr7uBw8RG0c9DuDOPo1sRv6Uy%2BF8svLf4Xh%2FgBki0IxyvUylsBgZrr6szhv70z%2BaQl5%2BRzpeF4FOuslofQ%2F%2BCBCRup7a8O1X%2FBMEkGG7g%2BalQK9J%2FnWnzV%2BA9mIAShOSxQ0l2MqR20A%2BOlhVwRGwFo1nfgZOuXZf0P%2F1Mlv%2FhdsoMI7Twc8GOqUBBhTs7AA8NjpKRLS3SK4BP9q4FJTj8Kbgwqk7L%2FobkIXbS9T4O5YMf9sezIv4LOJrqe7RIcPd4l%2BvMvgncmEwngJq2%2Bsd23zJKeSXQ4kyNE3498VCWiI%2FnuHfTRlVj8ygvyZlOKDrua0Oe1dX4HdUbAvTacPK7oa1WId3I1%2F9BQDiZ93ezXT5rYBsIBTMAlcfFg43Rg4uPpj0pdbemlsHABzPpXTn&X-Amz-Signature=c317aa1d889fc4edfaf8d995eb8175cdbebb0e682c8500c1cb24bdb010646a3f&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



Port 443: HTTPS

HTTP method: GET



![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/dc56f68d-8daf-4b31-bc04-5bd2547ffac9/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466US7POWYB%2F20260428%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260428T081529Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBAaCXVzLXdlc3QtMiJHMEUCIQC%2FgtcQlwliQGejGV%2BKfRDFqrqfOzGo4%2BXJtRq0CwmckgIgb092wDGYVrX%2F819CJBhMKLb3WxAh2vFmK%2Bh8v%2BwXzF0qiAQI2f%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDM7VqUb0RAK%2BXgn98yrcAzuQ24qlkqYtQVTMyondgGDDZv7C39WkYfZO1jlBIJWP2%2BVFo4l%2BiBmts33M5md5XJ4rnpIqp%2FAkghiQmtkaGNIbaHX6Ycgr50OModf16Y0EsSMIpefqKSy5Bn9WFeR3gZGVO84lU%2BPiQjqlOTUoS8nJ7tgGMzmjYPv8CZXJtg7R6vvumTqPXWVTNVDJg0IHY73QM2dBQqbuylC5CDLj4OwossJmzNtWclYVKYgTMLwhoYpFrlx7hnI%2FtTLP6bLXnbvehSVZexdxgadCMmFSyf8YigKnSZT%2BWMx1hkZyob%2B6NL4o8ovL3RhT2l7TdAgA63BGxKZJzasQt%2BleID8Z%2FULg2BGGI8zps%2FEQcw0nmI3dyLKfD94s%2FG3kbhX7XUytyhp370I01RA%2FH6jaLkkqs3eGaoVvef7wB19FXXxSio0rs109t5rA5MVeTOC46MX1OqdF1JoO2nh5uqxnHr7uBw8RG0c9DuDOPo1sRv6Uy%2BF8svLf4Xh%2FgBki0IxyvUylsBgZrr6szhv70z%2BaQl5%2BRzpeF4FOuslofQ%2F%2BCBCRup7a8O1X%2FBMEkGG7g%2BalQK9J%2FnWnzV%2BA9mIAShOSxQ0l2MqR20A%2BOlhVwRGwFo1nfgZOuXZf0P%2F1Mlv%2FhdsoMI7Twc8GOqUBBhTs7AA8NjpKRLS3SK4BP9q4FJTj8Kbgwqk7L%2FobkIXbS9T4O5YMf9sezIv4LOJrqe7RIcPd4l%2BvMvgncmEwngJq2%2Bsd23zJKeSXQ4kyNE3498VCWiI%2FnuHfTRlVj8ygvyZlOKDrua0Oe1dX4HdUbAvTacPK7oa1WId3I1%2F9BQDiZ93ezXT5rYBsIBTMAlcfFg43Rg4uPpj0pdbemlsHABzPpXTn&X-Amz-Signature=a3ebc17b1b5f30ccb7589401cf7e0c7cff2ef4b4361465ace2c276ebeaaa0e93&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)





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







