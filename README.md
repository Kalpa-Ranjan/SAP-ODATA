



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


![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/de3257b0-99da-4a97-9108-71d731170890/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XU33I7UT%2F20260527%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260527T093619Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCWMzx6AOlW1G4%2BVVKGlS1kqlmXkLyvck%2FyV4VpXiF0mQIhAKtzkPFhOG49FaC1055A%2BilG5RG6CWtLNbmFjzJUOVrGKogECJH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgwCByF3fx3SdJkEhXYq3AP3ksxYynrVMp8HK41AWIwBSoaBPHxc5tw9fg6dC7mg%2B6V0pEWEM5TEzUJl37ctQI6f0a36Pe7GxjGxqFvhTrXBfzT5LA8b2q6FigqwRp2R1egocyYLYRHLvsukhX6nJk69f%2FI2%2BwRMldwwr%2Fz%2Frr07OEuxr9y6bEdxWne2eiXGaCFYSZjKuvkT2jbY%2BJku7O%2FEz4KaRbs1gKadueeRl%2Brpz5bp5AnS7nlTcSzv%2BOEkUkQM2pZdh7IKF5akcpqT5fZe%2BMa8VBFErzVxvziIh%2FkZltu9H10jT%2FAVCu60mZkbdhIejASFd7dqw78B4w8spLInFSyPEoS3vEUsUNC1P6xHGRBV50oE5%2FFQ0vSlhyK7LS%2FScqr%2B0ADEHUw5nyb8Vp%2BPy%2FbwxaxQc1bp8EOPz1DkCr3DqQsP4MDTRsUKwGOGzy1LkqFK6zDmTv2R0FYiP7HQMPBvoXykiz%2FY3iarLl%2F6gf5RRPE3uyJ3kTRthy6QICp04GRVvMSf1CbG7i1qzxYF4glwkQvkG01LR1xNCp6D1w9GTcqDaHTgMF7bfi4kAd0H7nngPuYYlgmpq6%2F%2B%2Faf2x3dYvxENs9ZeD%2BIZDu3DBgbpyVpyczBHfEzyz3RLEwfcTAtmL1FW9o5LdDDev9rQBjqkAWEqdz93iDlGUxNjctP1GOwdRKPNKuQ5J7HxreWWic9DhvXJCRjw%2F2wyAkOcoSiAhl0%2F9BD8THFfP2Pz%2BUTD1ZMj%2FSk23KpgcxNjBa82CIrGQ2HmKX%2Bls0cy24pu0E%2BTKBQmvfktLbXLR4nsaHN%2BqFwpELDt83Kf1orauZeyutZf7MfxunrUzT4iHJtqa8m6zot5GWpD%2FmHTWrnDARCAw6xePtus&X-Amz-Signature=f5ced00048cac84c8b68f52935ecb27abc17f482f37082e1e2664106e6656bd0&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



Port 443: HTTPS

HTTP method: GET



![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/dc56f68d-8daf-4b31-bc04-5bd2547ffac9/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XU33I7UT%2F20260527%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260527T093620Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCWMzx6AOlW1G4%2BVVKGlS1kqlmXkLyvck%2FyV4VpXiF0mQIhAKtzkPFhOG49FaC1055A%2BilG5RG6CWtLNbmFjzJUOVrGKogECJH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgwCByF3fx3SdJkEhXYq3AP3ksxYynrVMp8HK41AWIwBSoaBPHxc5tw9fg6dC7mg%2B6V0pEWEM5TEzUJl37ctQI6f0a36Pe7GxjGxqFvhTrXBfzT5LA8b2q6FigqwRp2R1egocyYLYRHLvsukhX6nJk69f%2FI2%2BwRMldwwr%2Fz%2Frr07OEuxr9y6bEdxWne2eiXGaCFYSZjKuvkT2jbY%2BJku7O%2FEz4KaRbs1gKadueeRl%2Brpz5bp5AnS7nlTcSzv%2BOEkUkQM2pZdh7IKF5akcpqT5fZe%2BMa8VBFErzVxvziIh%2FkZltu9H10jT%2FAVCu60mZkbdhIejASFd7dqw78B4w8spLInFSyPEoS3vEUsUNC1P6xHGRBV50oE5%2FFQ0vSlhyK7LS%2FScqr%2B0ADEHUw5nyb8Vp%2BPy%2FbwxaxQc1bp8EOPz1DkCr3DqQsP4MDTRsUKwGOGzy1LkqFK6zDmTv2R0FYiP7HQMPBvoXykiz%2FY3iarLl%2F6gf5RRPE3uyJ3kTRthy6QICp04GRVvMSf1CbG7i1qzxYF4glwkQvkG01LR1xNCp6D1w9GTcqDaHTgMF7bfi4kAd0H7nngPuYYlgmpq6%2F%2B%2Faf2x3dYvxENs9ZeD%2BIZDu3DBgbpyVpyczBHfEzyz3RLEwfcTAtmL1FW9o5LdDDev9rQBjqkAWEqdz93iDlGUxNjctP1GOwdRKPNKuQ5J7HxreWWic9DhvXJCRjw%2F2wyAkOcoSiAhl0%2F9BD8THFfP2Pz%2BUTD1ZMj%2FSk23KpgcxNjBa82CIrGQ2HmKX%2Bls0cy24pu0E%2BTKBQmvfktLbXLR4nsaHN%2BqFwpELDt83Kf1orauZeyutZf7MfxunrUzT4iHJtqa8m6zot5GWpD%2FmHTWrnDARCAw6xePtus&X-Amz-Signature=4e3c9371a730d417a15683793fb7fed54dee965060d4601b4cde9407bbf19f92&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)





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







