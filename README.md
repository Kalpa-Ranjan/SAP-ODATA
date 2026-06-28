



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


![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/de3257b0-99da-4a97-9108-71d731170890/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466U5E7F5M7%2F20260628%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260628T191103Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIHMm%2BSb8FdCm2eUp2EO5nMbTJ8izpsZzi%2BXxDiJzHCBJAiEAt3JRya6cVUAXDcbIJ7OF5WpQWSkjiVEJ%2FnjBjSBbskUqiAQImv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDPmTeS%2BpArtB5fDbDyrcA0%2BzVZJJJ0m1rP16e%2BSl65su4zuI31uLbNBdBh1lHxjiNSgvSco0kcgwESU%2FOl%2BFx7JESdhUpXqa%2BWVMtSROYf2eZT1g5uo6mKuhsbCk1sdSQZVc6SVTa009dqdMIZ%2FuWicQH07%2BfU13ab9UaxWWq8p0V14Buvhw4isEAFK6ZR7PlXgADp6l5JEWG1GQ9PhpRqdW%2B2ND4OVtXVfV2KMCStAC1N70i7BqlS7jEXKSdQldKisH2QHBj4qZ6H7AO1otehs0eSDz8RRitNo7R%2BVoGHQ%2Fe5ycVytsieA7557vFmmXL%2F2s4W7G7bKGbEeOhFOluGX5oFDWurC8ZpyJWG3wMSLKLLOkJksNkCPMWOFWxIPs%2BriZTP3ca8CWanNwDxvJ%2FpkCcgqSgjER5iib4b2i2kdWIr0XjvtI3FwZwXz%2F%2Fb%2FvPWdcWUSPkkUt07gXv6grSHpQH8QRXJ3rtT964ooRUxwNDjaguyFzwPw2Myt%2F%2FJLtvxKbbDKGZNWMJWGKTYP%2FFTDFlmFKSY6fZKWrHvM5nh3oYAGNbcX6XzxGWTkUwa0GXXHVmrihKOTDKMcFesf3Kg329jf4m%2FjFTSX5EZQShEvpAAB7oQ85yiNiQHGpz4gux5w1pT4AfsloqcRbMMawhdIGOqUBUseiyHGpjGrPFNG3x1ZUrsP3tW1JkHhJ1urU%2F%2B01vflp6x1Ck6TYNKoeKect2w0QYrBUCP1z22dtNWDrTGEElwk%2FyYQp%2BCAComnshD8z04pvqjclA8Qg5%2Bqv%2B5RoXg%2FPPiXIuHNLqp1ai2TXinC2gy7DTVvrYrIgmX%2FKxdQINvn7GDWVzDPkAk%2BTvQRjm6L76n1IUCZNH3xvI521C5l4hGj9Y%2BCo&X-Amz-Signature=2c97c97b19335cd8c2671b821f7e0c75512febdf401cb8239c46d319cc885453&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



Port 443: HTTPS

HTTP method: GET



![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/dc56f68d-8daf-4b31-bc04-5bd2547ffac9/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466U5E7F5M7%2F20260628%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260628T191104Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIHMm%2BSb8FdCm2eUp2EO5nMbTJ8izpsZzi%2BXxDiJzHCBJAiEAt3JRya6cVUAXDcbIJ7OF5WpQWSkjiVEJ%2FnjBjSBbskUqiAQImv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDPmTeS%2BpArtB5fDbDyrcA0%2BzVZJJJ0m1rP16e%2BSl65su4zuI31uLbNBdBh1lHxjiNSgvSco0kcgwESU%2FOl%2BFx7JESdhUpXqa%2BWVMtSROYf2eZT1g5uo6mKuhsbCk1sdSQZVc6SVTa009dqdMIZ%2FuWicQH07%2BfU13ab9UaxWWq8p0V14Buvhw4isEAFK6ZR7PlXgADp6l5JEWG1GQ9PhpRqdW%2B2ND4OVtXVfV2KMCStAC1N70i7BqlS7jEXKSdQldKisH2QHBj4qZ6H7AO1otehs0eSDz8RRitNo7R%2BVoGHQ%2Fe5ycVytsieA7557vFmmXL%2F2s4W7G7bKGbEeOhFOluGX5oFDWurC8ZpyJWG3wMSLKLLOkJksNkCPMWOFWxIPs%2BriZTP3ca8CWanNwDxvJ%2FpkCcgqSgjER5iib4b2i2kdWIr0XjvtI3FwZwXz%2F%2Fb%2FvPWdcWUSPkkUt07gXv6grSHpQH8QRXJ3rtT964ooRUxwNDjaguyFzwPw2Myt%2F%2FJLtvxKbbDKGZNWMJWGKTYP%2FFTDFlmFKSY6fZKWrHvM5nh3oYAGNbcX6XzxGWTkUwa0GXXHVmrihKOTDKMcFesf3Kg329jf4m%2FjFTSX5EZQShEvpAAB7oQ85yiNiQHGpz4gux5w1pT4AfsloqcRbMMawhdIGOqUBUseiyHGpjGrPFNG3x1ZUrsP3tW1JkHhJ1urU%2F%2B01vflp6x1Ck6TYNKoeKect2w0QYrBUCP1z22dtNWDrTGEElwk%2FyYQp%2BCAComnshD8z04pvqjclA8Qg5%2Bqv%2B5RoXg%2FPPiXIuHNLqp1ai2TXinC2gy7DTVvrYrIgmX%2FKxdQINvn7GDWVzDPkAk%2BTvQRjm6L76n1IUCZNH3xvI521C5l4hGj9Y%2BCo&X-Amz-Signature=33bcf1bf86cdb149498a3eb0ec2fa817ce229e805dc4689ffa47eabb94ae15d4&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)





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







