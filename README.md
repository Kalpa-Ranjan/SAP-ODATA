



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


![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/de3257b0-99da-4a97-9108-71d731170890/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZMJ5AV4J%2F20260316%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260316T185512Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBAaCXVzLXdlc3QtMiJIMEYCIQDB%2BLieqt9twG1X6Px%2FiP6Q5DK1Hle2Gl48ffwhuhHKygIhAJBAKd%2BqtVb6hBHg%2BWz7l0dn0lTxRmBpO2exnvWizlXaKogECNj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgyMlex9ctIxeh98gmIq3AMDbW4uNjLu1OWsv622%2BP94SqQRyvLksFh0QfnzGu%2FbAHS77ZNNbId7LArZCRujFOe0%2FB2y0lC44bQ%2FRerLc9ez8FpodyEVpdU9UDvySHascULtMdEdlSi8artoApv2b6EZdGFgbi7d%2B9bPNu0a5qK6IPBMKo9r86QLH%2Fz%2FaNrRbwl%2FteO2l7ow0qk1QpvoW4Wt%2BQJQZMEMRbxoqnAD3UK5HOETOMOU5PIHiaOPxx3xqmgaPRq8vdx63S3YaxSyh2pgmw9VQkb01f6n4b0MZirVggAi7uRaA9OK7zmq2CNVaH0U61QEtfgJvQE1MtEVsmRjBN31ImzYnjZjB%2BkdUZsjmenWzFFWODmB3qtCV2CzLdnLz75J0FqbM0xyjIbMThbrPJnSfSwvfU9Vshgio6A4iDczJ3yglbwwQdxIpYd8x5IV3qxS7%2BC8riqk4movZ%2B3cp%2FJWxtqRM3wJRFZnjC83LskyYiJ9qlrxoLLBB%2BU6kjUvRoxiQ0svyPnaIMVqvrc5RFMluvkyBJaLKacNrEhbYEtu2U5wIDRXrN4tQR5LrZiir45oUe8LOToFfnHu0k288NpmLBtDetyAkr6iNOiZLbPuBXULQGdtt9DNmqTztHv2hxLT7U74eOKWBDCivuDNBjqkAeBuq0hW9f3X6oQd1ZAskLfpZ4TzhaCxWtQSP7wbU0ezlc0Cd21dKZp%2FERPcWWF2Hu%2FIFSZHsx9zHNZfmKCLfKzop8gfPEsv9tb8%2FzeY73i96Q2uzRiCjhvbBq9SMALZ%2Bg9Vd7e7vuyJCd%2FsxDxtCNaEVHdI71vyLmX12%2F5To%2FrF1UN1n0nvdxPby%2FhWKfFtRYDJlaQxo9V0GiNaX8uHCOslKSje&X-Amz-Signature=99b2ce8019bdd9088955a5036572f1251c5b403f8f811cc39b5cba6565a5b4c5&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



Port 443: HTTPS

HTTP method: GET



![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/dc56f68d-8daf-4b31-bc04-5bd2547ffac9/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZMJ5AV4J%2F20260316%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260316T185512Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBAaCXVzLXdlc3QtMiJIMEYCIQDB%2BLieqt9twG1X6Px%2FiP6Q5DK1Hle2Gl48ffwhuhHKygIhAJBAKd%2BqtVb6hBHg%2BWz7l0dn0lTxRmBpO2exnvWizlXaKogECNj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgyMlex9ctIxeh98gmIq3AMDbW4uNjLu1OWsv622%2BP94SqQRyvLksFh0QfnzGu%2FbAHS77ZNNbId7LArZCRujFOe0%2FB2y0lC44bQ%2FRerLc9ez8FpodyEVpdU9UDvySHascULtMdEdlSi8artoApv2b6EZdGFgbi7d%2B9bPNu0a5qK6IPBMKo9r86QLH%2Fz%2FaNrRbwl%2FteO2l7ow0qk1QpvoW4Wt%2BQJQZMEMRbxoqnAD3UK5HOETOMOU5PIHiaOPxx3xqmgaPRq8vdx63S3YaxSyh2pgmw9VQkb01f6n4b0MZirVggAi7uRaA9OK7zmq2CNVaH0U61QEtfgJvQE1MtEVsmRjBN31ImzYnjZjB%2BkdUZsjmenWzFFWODmB3qtCV2CzLdnLz75J0FqbM0xyjIbMThbrPJnSfSwvfU9Vshgio6A4iDczJ3yglbwwQdxIpYd8x5IV3qxS7%2BC8riqk4movZ%2B3cp%2FJWxtqRM3wJRFZnjC83LskyYiJ9qlrxoLLBB%2BU6kjUvRoxiQ0svyPnaIMVqvrc5RFMluvkyBJaLKacNrEhbYEtu2U5wIDRXrN4tQR5LrZiir45oUe8LOToFfnHu0k288NpmLBtDetyAkr6iNOiZLbPuBXULQGdtt9DNmqTztHv2hxLT7U74eOKWBDCivuDNBjqkAeBuq0hW9f3X6oQd1ZAskLfpZ4TzhaCxWtQSP7wbU0ezlc0Cd21dKZp%2FERPcWWF2Hu%2FIFSZHsx9zHNZfmKCLfKzop8gfPEsv9tb8%2FzeY73i96Q2uzRiCjhvbBq9SMALZ%2Bg9Vd7e7vuyJCd%2FsxDxtCNaEVHdI71vyLmX12%2F5To%2FrF1UN1n0nvdxPby%2FhWKfFtRYDJlaQxo9V0GiNaX8uHCOslKSje&X-Amz-Signature=0d51934c229f1952aedcfda05fa8b5e088b737a484ea054c69481eeb1ecf16ec&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)





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







