



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


![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/de3257b0-99da-4a97-9108-71d731170890/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662FHX7A34%2F20251108%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251108T010817Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAAaCXVzLXdlc3QtMiJIMEYCIQDjwvbxSS7vCryE5F3ORp%2Fry3OwacYFoKMUMm%2BV%2By2B5QIhAJizPaUXff1VuBEHUkk%2FkZO2dCHh%2FwdJU5Sb1vawR3B6KogECMn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgwSvOZf%2BKLRliNVBTAq3AO7SFYsuvvb05uE92S0tCSQ2%2FsOh1oUcpoI8QD%2BBDYX5b9sZO2mnOJUfh9EJ9iRGPc5%2FYuoKmcJ86BX2IM4vRPVVLuqy7QzRtQ7X0bc5zIluyxT3joOK037Qqf6MxdSedZ5r1hAK%2F2H8hIL%2B8qKuRs%2F5AAb15K5PbuLw4bUN6CoQCdiJ%2B5gx6b2OADvgilOCT%2BI5qL2rkQKuWSM7M3duNBKrCfLz7pUz4rFR6f699VJBz%2Bh%2FZbJbkGGZD%2FoWbhkHJGtfUwjmX6wwnEpNQQdQT3DBR7Lt472xqD2WV3rNkA5UdczeOqQYMVbD0zSsn6WRi22ALxb8UcoN8ACRXrp9txDR2zUdtaKFIv45BLgv57HkejQQ1qNSf9CBfnKL58TZoBTzWRpRIQhHTH2ZrlHDlvPcZ2D7UwhjF2m9hPp%2BWL6IPEKFvezAo%2BnZMxnor27wJ8UkYkwkACGVKQWHHApVEYlQqLaJP3SELEPhSDEFou5WPZtXkta9Yui6Ccp6sPyk%2Bl1lu8PRak7pcJ%2BkSi%2Bx35Grgjsav0hhAv46eDt5DM3T7TWqXuiqHBGKDMshXlXWxZQxfqKoKxdImNsCdMR8WpTooWaYzzxp3aFMqXzOfnKSREHn8CITyYQ25KT9TCikbrIBjqkAbP%2Fp65mHBBRFedNM3VIKEjFi20QaBILOvZ3RBkrtLhmV37IB5ZvBiPaIeO8bpKsCu7zrASeCFSxHM4mvxXQKumKa6plg9Gxm01rtRIS6Dt3xqHUbpi794B6Q%2FwtOdCH51zFCm2uhkh%2F3OiCReHOK%2B3jgsyl5XDW%2BUsqr0IjusVgTLXc8tf%2BqtBLANwSLty5tubQ7KYNC45s937XWSGlwUvjAhuU&X-Amz-Signature=c391f7756f9d5da38c9e4a5228018cf47193add53528363575f5a9b70d30cb57&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



Port 443: HTTPS

HTTP method: GET



![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/dc56f68d-8daf-4b31-bc04-5bd2547ffac9/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662FHX7A34%2F20251108%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251108T010817Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAAaCXVzLXdlc3QtMiJIMEYCIQDjwvbxSS7vCryE5F3ORp%2Fry3OwacYFoKMUMm%2BV%2By2B5QIhAJizPaUXff1VuBEHUkk%2FkZO2dCHh%2FwdJU5Sb1vawR3B6KogECMn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgwSvOZf%2BKLRliNVBTAq3AO7SFYsuvvb05uE92S0tCSQ2%2FsOh1oUcpoI8QD%2BBDYX5b9sZO2mnOJUfh9EJ9iRGPc5%2FYuoKmcJ86BX2IM4vRPVVLuqy7QzRtQ7X0bc5zIluyxT3joOK037Qqf6MxdSedZ5r1hAK%2F2H8hIL%2B8qKuRs%2F5AAb15K5PbuLw4bUN6CoQCdiJ%2B5gx6b2OADvgilOCT%2BI5qL2rkQKuWSM7M3duNBKrCfLz7pUz4rFR6f699VJBz%2Bh%2FZbJbkGGZD%2FoWbhkHJGtfUwjmX6wwnEpNQQdQT3DBR7Lt472xqD2WV3rNkA5UdczeOqQYMVbD0zSsn6WRi22ALxb8UcoN8ACRXrp9txDR2zUdtaKFIv45BLgv57HkejQQ1qNSf9CBfnKL58TZoBTzWRpRIQhHTH2ZrlHDlvPcZ2D7UwhjF2m9hPp%2BWL6IPEKFvezAo%2BnZMxnor27wJ8UkYkwkACGVKQWHHApVEYlQqLaJP3SELEPhSDEFou5WPZtXkta9Yui6Ccp6sPyk%2Bl1lu8PRak7pcJ%2BkSi%2Bx35Grgjsav0hhAv46eDt5DM3T7TWqXuiqHBGKDMshXlXWxZQxfqKoKxdImNsCdMR8WpTooWaYzzxp3aFMqXzOfnKSREHn8CITyYQ25KT9TCikbrIBjqkAbP%2Fp65mHBBRFedNM3VIKEjFi20QaBILOvZ3RBkrtLhmV37IB5ZvBiPaIeO8bpKsCu7zrASeCFSxHM4mvxXQKumKa6plg9Gxm01rtRIS6Dt3xqHUbpi794B6Q%2FwtOdCH51zFCm2uhkh%2F3OiCReHOK%2B3jgsyl5XDW%2BUsqr0IjusVgTLXc8tf%2BqtBLANwSLty5tubQ7KYNC45s937XWSGlwUvjAhuU&X-Amz-Signature=47bf902cb22c7fdc60dd869e2803627f3a39f58f56db22156fa63f6c8f20e08d&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)





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







