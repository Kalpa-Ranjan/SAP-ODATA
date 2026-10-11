



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


![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/de3257b0-99da-4a97-9108-71d731170890/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WIIAVNRQ%2F20261011%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20261011T002526Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIA%2F52chhlahXV4fGOPJeHVaWc1JApvkZpLiUw50u%2BaQoAiBrspWW99e97qU1m2x44Wa3zmePECRgxCUOkK8dd%2B87Syr%2FAwheEAAaDDYzNzQyMzE4MzgwNSIMS53FHTA%2FdzTavYWsKtwD2gBtcfAVYyNLAjdria8mnH7CZcxVolmSCVl7LAPPEuCgLS0xUk4IE1m6Cy%2BNkbSXSb5OE7iw4ssLG1waI1MN6ERnG0LwvVgB41ONuPSs%2FISlOdCziWNvhNW7AUaz0yYN9KNaUdYV0d99H8j88IVrmQImBAsr2A493TbR9KvvkMChsnUoDSvW7QS%2Be%2F0HROryZqcmgo2%2Fptm5HpKCp5dVtUqnqsv2s8%2BCgcECx41CGmCizyuuySln3gmM1lrz10V8TZos5Q%2F%2BRyYjXrr%2BcKRvkO377%2BDVPqof5Wgv3FhiuuyUQsJLiV%2Bhyke587c0UWF1rVKdQVVxtqBpbl9EULJvPpl36R%2B6jisYqjFeWOVvNmJ30qF%2B64IuWzjg0bhk8znQUdosJi4fGL6Fv1Fzl5z%2F6kw6nLdUqmCFER%2BXJ8iXwoP%2FOUOSEKi7ZMHxSVfw21FUNv1D9YsvJxxW7%2B2vMtT2umdKq9Yro9wcCKUDbuKwqajQssvitlfAvcco18WT4hLP0HIir8pHW7g8k%2BIuPd%2FtRmAsdgBE2D844ghaXKaCkuN56Bsst%2FeqQxhxXjvl1pGInaCwbHETE0nWYYvmp69hyxtbbCuc55sxzN%2FfqrM7CH8pJv7NdCd%2BfTSUfoww79mq1gY6pgHq6IWPNcwci%2F2%2F%2F%2B3TtG8OSIDYFaSJ1%2FjpxzJWNATdmJd5Zb37RRn3kE940PGyEeae%2BmU3kQ0lSagPolsE0BxNpwHrAKFhH69yLgzuHW97a98sxbCfqNNoqcMMFy5USZJ3arZvhBCpi7RhyjTMzAmnZ9j2HY7%2Fb6S%2BZYlJ2DSqb28KNflihLWdqvHCUISdqO0t7LHFbjSGCvcbXpGR5ZFkQu3DF2Yz&X-Amz-Signature=0cd2efac17d6e493261d5e14c24092b7b980adacb06b18b659aac9e3c64fb08a&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



Port 443: HTTPS

HTTP method: GET



![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/dc56f68d-8daf-4b31-bc04-5bd2547ffac9/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WIIAVNRQ%2F20261011%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20261011T002526Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIA%2F52chhlahXV4fGOPJeHVaWc1JApvkZpLiUw50u%2BaQoAiBrspWW99e97qU1m2x44Wa3zmePECRgxCUOkK8dd%2B87Syr%2FAwheEAAaDDYzNzQyMzE4MzgwNSIMS53FHTA%2FdzTavYWsKtwD2gBtcfAVYyNLAjdria8mnH7CZcxVolmSCVl7LAPPEuCgLS0xUk4IE1m6Cy%2BNkbSXSb5OE7iw4ssLG1waI1MN6ERnG0LwvVgB41ONuPSs%2FISlOdCziWNvhNW7AUaz0yYN9KNaUdYV0d99H8j88IVrmQImBAsr2A493TbR9KvvkMChsnUoDSvW7QS%2Be%2F0HROryZqcmgo2%2Fptm5HpKCp5dVtUqnqsv2s8%2BCgcECx41CGmCizyuuySln3gmM1lrz10V8TZos5Q%2F%2BRyYjXrr%2BcKRvkO377%2BDVPqof5Wgv3FhiuuyUQsJLiV%2Bhyke587c0UWF1rVKdQVVxtqBpbl9EULJvPpl36R%2B6jisYqjFeWOVvNmJ30qF%2B64IuWzjg0bhk8znQUdosJi4fGL6Fv1Fzl5z%2F6kw6nLdUqmCFER%2BXJ8iXwoP%2FOUOSEKi7ZMHxSVfw21FUNv1D9YsvJxxW7%2B2vMtT2umdKq9Yro9wcCKUDbuKwqajQssvitlfAvcco18WT4hLP0HIir8pHW7g8k%2BIuPd%2FtRmAsdgBE2D844ghaXKaCkuN56Bsst%2FeqQxhxXjvl1pGInaCwbHETE0nWYYvmp69hyxtbbCuc55sxzN%2FfqrM7CH8pJv7NdCd%2BfTSUfoww79mq1gY6pgHq6IWPNcwci%2F2%2F%2F%2B3TtG8OSIDYFaSJ1%2FjpxzJWNATdmJd5Zb37RRn3kE940PGyEeae%2BmU3kQ0lSagPolsE0BxNpwHrAKFhH69yLgzuHW97a98sxbCfqNNoqcMMFy5USZJ3arZvhBCpi7RhyjTMzAmnZ9j2HY7%2Fb6S%2BZYlJ2DSqb28KNflihLWdqvHCUISdqO0t7LHFbjSGCvcbXpGR5ZFkQu3DF2Yz&X-Amz-Signature=b96e7606313b88289c15f6445c8e1aafb0954fc9bb319b0bf86277e365443900&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)





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







