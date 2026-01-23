



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


![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/de3257b0-99da-4a97-9108-71d731170890/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SFLVVHFI%2F20260123%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260123T123726Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEC0aCXVzLXdlc3QtMiJGMEQCIEIoc5dww%2F5ecxPK51rDeuEhKV5IuGTXPX47eiwOHmt%2BAiA7ZFBtjcu2zgQPVMPJ2FG5zAv0ibESPlf34566U67f8yqIBAj2%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMNoxuu8Wg7MpgEWM1KtwDoRHDOJrc4FVTXyK30HDwuWngbcvBdTUaN%2Bk28wr9plz59yruohVN5m%2BiH20e%2Bs2Oi3dN%2F7czhZ%2BL4JvgIFf4x2uShXaueEN6cxMUCzhaAlKpId5griMA2XH5ZDRh%2Flv52jJx2RTY3mwbQNIEfdOK8GfbKno2fygmCGh1QWKpI%2BV56KhWkVrM4YNpCB5Npn5CZgJlQxPBQUbqSNRPkJ5XFPISon4TqUJMHSiMGQAzWSyJPn462Y0DR2AguzSIGzAKqszRS5xPSNuGdRb%2BFCwX17RI17hYliyLD2%2FHEIF%2FYl0uvAM%2BaKjjqtwlM%2FlwQF1cn8an37PaCDYFC2XarAH9rOrPsWSzYbedLLKVSQsxfARznFjY4u2RUO5fSbGsiiz%2F9%2FaiVlymAJT50wtrt5VLsQjQLwzp1EzIDB8JwntgDKYtGIylNcHz7Thx7skTOQ2pMP3lSQJ5SRMYWygfo9MeroR4xpavaX2ze7XpGNttQ4b8rZYFxjxSdtBG5cPhA9i0TB1FmFnyJEv8PkudUE%2FYC%2FJ0rZDHSrf0D9nDQ%2Fuy2dtF%2B43s0DA%2FtGZa%2FPcy8FbXw%2FhjbrMCaBUEuvdgIr5JaukDdGtMXW15Ws8VnXA5KYo5%2FseUWRq%2BsT7qWpEwytXNywY6pgGctegiRNVM6z4aFmNkPm5ODh6mp3jVlpG8RQG8cd%2FFkdh2g7iHr64qD0nKODhqZrKhLKZf5hCkTixSkoZsPxWGIz3CeNm1K8un%2FmmchXwgSk7fiEQs%2BdrlzW%2BPxJa2WOcAG1ebfXeZL5r%2FrLBCvJ1rINXEDxOwCTBQqZNly7N5mMTXFIn2NXT0qH%2FfN6pEP8tXZaqopcKuWDfzmsLLTX4KsuNSC1%2FE&X-Amz-Signature=8db1e5faf30bf54188ab500a38c5d39c5504f5ca28777ccb3612d4fae89e81a4&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



Port 443: HTTPS

HTTP method: GET



![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/dc56f68d-8daf-4b31-bc04-5bd2547ffac9/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SFLVVHFI%2F20260123%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260123T123726Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEC0aCXVzLXdlc3QtMiJGMEQCIEIoc5dww%2F5ecxPK51rDeuEhKV5IuGTXPX47eiwOHmt%2BAiA7ZFBtjcu2zgQPVMPJ2FG5zAv0ibESPlf34566U67f8yqIBAj2%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMNoxuu8Wg7MpgEWM1KtwDoRHDOJrc4FVTXyK30HDwuWngbcvBdTUaN%2Bk28wr9plz59yruohVN5m%2BiH20e%2Bs2Oi3dN%2F7czhZ%2BL4JvgIFf4x2uShXaueEN6cxMUCzhaAlKpId5griMA2XH5ZDRh%2Flv52jJx2RTY3mwbQNIEfdOK8GfbKno2fygmCGh1QWKpI%2BV56KhWkVrM4YNpCB5Npn5CZgJlQxPBQUbqSNRPkJ5XFPISon4TqUJMHSiMGQAzWSyJPn462Y0DR2AguzSIGzAKqszRS5xPSNuGdRb%2BFCwX17RI17hYliyLD2%2FHEIF%2FYl0uvAM%2BaKjjqtwlM%2FlwQF1cn8an37PaCDYFC2XarAH9rOrPsWSzYbedLLKVSQsxfARznFjY4u2RUO5fSbGsiiz%2F9%2FaiVlymAJT50wtrt5VLsQjQLwzp1EzIDB8JwntgDKYtGIylNcHz7Thx7skTOQ2pMP3lSQJ5SRMYWygfo9MeroR4xpavaX2ze7XpGNttQ4b8rZYFxjxSdtBG5cPhA9i0TB1FmFnyJEv8PkudUE%2FYC%2FJ0rZDHSrf0D9nDQ%2Fuy2dtF%2B43s0DA%2FtGZa%2FPcy8FbXw%2FhjbrMCaBUEuvdgIr5JaukDdGtMXW15Ws8VnXA5KYo5%2FseUWRq%2BsT7qWpEwytXNywY6pgGctegiRNVM6z4aFmNkPm5ODh6mp3jVlpG8RQG8cd%2FFkdh2g7iHr64qD0nKODhqZrKhLKZf5hCkTixSkoZsPxWGIz3CeNm1K8un%2FmmchXwgSk7fiEQs%2BdrlzW%2BPxJa2WOcAG1ebfXeZL5r%2FrLBCvJ1rINXEDxOwCTBQqZNly7N5mMTXFIn2NXT0qH%2FfN6pEP8tXZaqopcKuWDfzmsLLTX4KsuNSC1%2FE&X-Amz-Signature=586e6a113d385368a16c970015d5fabcf75cf0e37c56fb2542e85759ab19851d&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)





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







