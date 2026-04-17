



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


![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/de3257b0-99da-4a97-9108-71d731170890/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QA25QAU7%2F20260417%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260417T072500Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAcaCXVzLXdlc3QtMiJGMEQCIGniZ%2FJXiNdAeSantFTIyVqVbCbDJ51mKsdAk1fkp38RAiBnZ3vl8T0DipoLAhcyp1m0ZT3TS6jRvPH3yiBavazUhiqIBAjQ%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMHao%2FabURf1pflJ%2F6KtwDHOYlnjy%2FXbJdW2ZoK50xn%2FilHNQf8DNnIfJjgQ1n5yeemP8S4%2F7T07BK0HH3W4CVdWs37BSRR0PiQwKkdFD9dKWNGgwdRI3ilURSEmGFddLADgMP2MJm8YjZ599HBEwB0sBlzLToMBhgYeJPTJkjHWk%2BbfBUJy20753B390pbxTVkw9F9ly7M%2BG%2BGUqFHTa1Inq9%2BvPldeDgHxUoTcGAF02fnKRu52GXGVuitETjcbaoionA2QMyVGE1tCTwTFcfX0OOqOr3DWQ5ai7YRGaQ6SF4IcnJ79pb3Ab96ON7pA8v%2FlqohFnwTnHwdkDLCgzcI0Aw%2FT8HiLJlKMcnX0Aiy%2B%2BXnfSMODyNiJopO39ZHqKuaXSXBejt70OGMqXSkiJBAgz8Takicb0Yre%2B7RZhb26ipiz6mxVvdQ4Cl%2FtFnVNZcHRApBGM%2BnMHheR9YlbSecwSlIlo6T84aBTSXhlIhIvDAnFnFZZBZT6LjNMSVeeH4RJiT1QjpUVfmAdkayZkL%2FGB9AZRuhakeutnEPBDtcOAGOJIkyQmmAIZOQxKW6qAlaU6OPa3lLHuVl5MnC%2B3Gl8NTCn9aY8FTDjeoEk%2Fkiixi1zr3lD8QfJUjS4U%2BvJDqimy4NBOKmI299kkw1rmHzwY6pgE1rgoOfQL%2F5Ch1EXOg4NYQ%2FO34Of%2BGpkw4YTZDNGTpcglz3ChAipem2BfPUC7cPE8cwzuyqESb6y1zwvN%2BOnHcsUBrWVfw80%2FcoX3Q6P6vg7%2BJoLRLRVhPgXdZEl5y%2BB9U5d26QnbcWmLUEBegm4WXHvkqJf%2BRieVIJl1E4VZsBqNUON%2FzXUfdTsM2qG6pHnxFEU%2BtGvuTKzIgQocV2CiqyD9St0Do&X-Amz-Signature=d2120d36484079b34ab3d76702b22ec9d99a705b27a4e928ff940985c8190fbd&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



Port 443: HTTPS

HTTP method: GET



![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/dc56f68d-8daf-4b31-bc04-5bd2547ffac9/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QA25QAU7%2F20260417%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260417T072500Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAcaCXVzLXdlc3QtMiJGMEQCIGniZ%2FJXiNdAeSantFTIyVqVbCbDJ51mKsdAk1fkp38RAiBnZ3vl8T0DipoLAhcyp1m0ZT3TS6jRvPH3yiBavazUhiqIBAjQ%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMHao%2FabURf1pflJ%2F6KtwDHOYlnjy%2FXbJdW2ZoK50xn%2FilHNQf8DNnIfJjgQ1n5yeemP8S4%2F7T07BK0HH3W4CVdWs37BSRR0PiQwKkdFD9dKWNGgwdRI3ilURSEmGFddLADgMP2MJm8YjZ599HBEwB0sBlzLToMBhgYeJPTJkjHWk%2BbfBUJy20753B390pbxTVkw9F9ly7M%2BG%2BGUqFHTa1Inq9%2BvPldeDgHxUoTcGAF02fnKRu52GXGVuitETjcbaoionA2QMyVGE1tCTwTFcfX0OOqOr3DWQ5ai7YRGaQ6SF4IcnJ79pb3Ab96ON7pA8v%2FlqohFnwTnHwdkDLCgzcI0Aw%2FT8HiLJlKMcnX0Aiy%2B%2BXnfSMODyNiJopO39ZHqKuaXSXBejt70OGMqXSkiJBAgz8Takicb0Yre%2B7RZhb26ipiz6mxVvdQ4Cl%2FtFnVNZcHRApBGM%2BnMHheR9YlbSecwSlIlo6T84aBTSXhlIhIvDAnFnFZZBZT6LjNMSVeeH4RJiT1QjpUVfmAdkayZkL%2FGB9AZRuhakeutnEPBDtcOAGOJIkyQmmAIZOQxKW6qAlaU6OPa3lLHuVl5MnC%2B3Gl8NTCn9aY8FTDjeoEk%2Fkiixi1zr3lD8QfJUjS4U%2BvJDqimy4NBOKmI299kkw1rmHzwY6pgE1rgoOfQL%2F5Ch1EXOg4NYQ%2FO34Of%2BGpkw4YTZDNGTpcglz3ChAipem2BfPUC7cPE8cwzuyqESb6y1zwvN%2BOnHcsUBrWVfw80%2FcoX3Q6P6vg7%2BJoLRLRVhPgXdZEl5y%2BB9U5d26QnbcWmLUEBegm4WXHvkqJf%2BRieVIJl1E4VZsBqNUON%2FzXUfdTsM2qG6pHnxFEU%2BtGvuTKzIgQocV2CiqyD9St0Do&X-Amz-Signature=d8c3320138a00f48c89c4976e99ad1536c27784328f4a7882b9aeabfc50999ad&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)





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







