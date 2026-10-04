



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


![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/de3257b0-99da-4a97-9108-71d731170890/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VXD6A5SK%2F20261004%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20261004T135511Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCXiuH1qyk6sL2VLhh9mubLO1o%2F2eNQRFuN5DdmrsNR1gIgW8VYZpOZi%2FNivsPwYH9whZPLV8ha0OKffzRQya2sb%2BkqiAQIwf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDJWrBUH8hmkXtP6nMyrcA2SFM6FTp7b8CuVt5h3EhDzlsZNNk3S2kWwHy10Bb9oX9zgLIUF8FwJEkV0HjJdkZEvknRAM9eHpu1j%2BabdXMiqT5mMwYibq4fDcPV4d3Hz%2FRoh04j6JJ5JAokV2JDkY8h89UURcSP7RMqovPQifDt%2B40sIsGxsV2F4F91fYmc30dg4m8GMg1cHhfNLNwzuqkwOx1gIsVONJl4DYIgUFqsUMpcS4uC07ZRRdSbLBoikePNqlgfegAXThMT8KlAkK1pyffJZHrvfD34n8JqsPHFkYwVfU7LuE7Z67H2XkIY3UmoclHeYN54HFJNsMys6mJSAW%2FIxvkyXgWk7fXHDI9%2FLm%2FDqeUC3UMEiZ3RZSDgKX68DI5S4%2FsC4gbAVffzDeHe8gCqVUyIZKUgR8sf%2BXD%2BOFmfmqqDRqKqxbRLJs1fCzbUifKiJNfxwdIyXYwTSriS%2FxlD2oatb5W%2BXBHxa1grB9sWd%2BvF0CI%2BlZT2N%2Bk4iMTeIPhuaWNk%2BDcTPMRE80coG2V%2B8bgYDn6i20j2i46bRFdDhDF86yfNDnWJ%2FpJyahG8Z%2F%2FAEuvs%2F7Cr%2FOwgm9SFt9uO7y61BCN0rlov%2FBRtWlOxMPJtnsN0q0KfGY%2F6W8SFNuKsFQ3lZOVugUML2YiNYGOqUBvVwRL9YW6gXfTbV3Jo%2FT623q9pY7JErzRAkNNBIFgKIkOyWMUIgvjbL7jhC4k4y59kyNt60b0dANzxYi3Rv2W8axI1UOuRB21h8quera8ATWzuYn%2FHf04Suzxez9BdqiAC54FMCH%2FjUWJT4dUdkkZowiB9C0Wzwy99i%2BiJc7kdeXTTNDo3yjbu%2BuO0TsaBdyXoYqVSdJnu3jgc6oAwSVLoYvzioq&X-Amz-Signature=a2a086dcf1a149278223e696096eb6b3c1cc08ec125c21ccf0c27ac34eafe2ea&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



Port 443: HTTPS

HTTP method: GET



![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/dc56f68d-8daf-4b31-bc04-5bd2547ffac9/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VXD6A5SK%2F20261004%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20261004T135511Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCXiuH1qyk6sL2VLhh9mubLO1o%2F2eNQRFuN5DdmrsNR1gIgW8VYZpOZi%2FNivsPwYH9whZPLV8ha0OKffzRQya2sb%2BkqiAQIwf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDJWrBUH8hmkXtP6nMyrcA2SFM6FTp7b8CuVt5h3EhDzlsZNNk3S2kWwHy10Bb9oX9zgLIUF8FwJEkV0HjJdkZEvknRAM9eHpu1j%2BabdXMiqT5mMwYibq4fDcPV4d3Hz%2FRoh04j6JJ5JAokV2JDkY8h89UURcSP7RMqovPQifDt%2B40sIsGxsV2F4F91fYmc30dg4m8GMg1cHhfNLNwzuqkwOx1gIsVONJl4DYIgUFqsUMpcS4uC07ZRRdSbLBoikePNqlgfegAXThMT8KlAkK1pyffJZHrvfD34n8JqsPHFkYwVfU7LuE7Z67H2XkIY3UmoclHeYN54HFJNsMys6mJSAW%2FIxvkyXgWk7fXHDI9%2FLm%2FDqeUC3UMEiZ3RZSDgKX68DI5S4%2FsC4gbAVffzDeHe8gCqVUyIZKUgR8sf%2BXD%2BOFmfmqqDRqKqxbRLJs1fCzbUifKiJNfxwdIyXYwTSriS%2FxlD2oatb5W%2BXBHxa1grB9sWd%2BvF0CI%2BlZT2N%2Bk4iMTeIPhuaWNk%2BDcTPMRE80coG2V%2B8bgYDn6i20j2i46bRFdDhDF86yfNDnWJ%2FpJyahG8Z%2F%2FAEuvs%2F7Cr%2FOwgm9SFt9uO7y61BCN0rlov%2FBRtWlOxMPJtnsN0q0KfGY%2F6W8SFNuKsFQ3lZOVugUML2YiNYGOqUBvVwRL9YW6gXfTbV3Jo%2FT623q9pY7JErzRAkNNBIFgKIkOyWMUIgvjbL7jhC4k4y59kyNt60b0dANzxYi3Rv2W8axI1UOuRB21h8quera8ATWzuYn%2FHf04Suzxez9BdqiAC54FMCH%2FjUWJT4dUdkkZowiB9C0Wzwy99i%2BiJc7kdeXTTNDo3yjbu%2BuO0TsaBdyXoYqVSdJnu3jgc6oAwSVLoYvzioq&X-Amz-Signature=772e2853707ac62a09af3cfdeb6d5b0e401cb845b8bba4ce3fec237bcd33dd31&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)





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







