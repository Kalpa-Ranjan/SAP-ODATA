



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


![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/de3257b0-99da-4a97-9108-71d731170890/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46663I3I45Z%2F20260110%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260110T011658Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIGAywAAt%2BapN0dpKJ53WHmVCCp1%2BGwQhfF23N3tLDtqDAiEAlJqAIz3w0ypLBk%2FBVqeYC75DurKW4G%2BYX2o3Yb1xebEqiAQIsv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDEnveQjlbJUtJf3ZDSrcA%2BfYOwUfzOFKNHtQpCXqk2QqtsD24Gx16VTfD5yV4FxGDElU7UWCqtcckeVqxzS%2BDlRS037DBqceg%2Bw3c%2F%2BMltdkPHOu4jdsNBE1hN6lLxz3Bpj96yvt%2BAcXwLsAZOPbMN9uWMFuKE%2F2u94xHUHeaRup7ZFM49DLgcmVmp%2BLVpXTCDj8pwQHqQQaZgdXUe%2FZPc5dkznkYJ2%2FfPlXRVOnVqI8HCEejDaQ%2B1QTUhAj1i6kom8sNpMOmwECjY05VkuJIOeIKi5I5w9MUWRw8EKaRbo7gWgVi%2BjkgGXnYkSbOyTHkF5EZTKTmZlShrajJFnulRFh6eL6lyofK9mEMG4oa2Enw1wNm%2Bime4szeAMyYJoTGySkRhLQafOzLt1LSGucbwSJ0ahmyHUArp96sgMzn4jSSFIYWXPERjw8y1xWIBuB6Qb9IRSWWEh8DYF7G4iTXNxPbG%2FFpRpxbByOxMfVfOUBjH4%2B52ubU%2BEV3TAOd3kHY%2F2JmfZfWK%2B0jgafEa8c51xFDy66SijVsViEaWzl%2BaFjQeG5zRF7cMm2kuHKV5jacpKrIMgkOsVA2HWVkUhiQhtGzSIv5yTpQV%2BKlA44sfuZ4Cb6hyQ6CkqAYRhhXUHFefV9Mlf6D8vxeJFRMNLAhssGOqUBJ8L5g8GPtSy11HW%2BWhBRpzXkX9GQ73I343lJEPNVYAoFDNycmNWMHR1q7ppy16G2RGXksMsmT20s6QThkFIc%2FDpGfuxBl78%2FQYKLhJEzX9jiibaZEG3c0LeMwy%2BtsqVCQOBBGo7FFgm6UlvbpsKX7faywLKiycGa9wXcjphRXHvwJWVlDlkuKQv9zcKWk9QHViJcO5h2RHn5YI6yy6L2qIgnpmoz&X-Amz-Signature=c755fe7bb793d5b0aa46fc743d6ca9fa343d6083d6e73d472a83f7018ee21bde&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



Port 443: HTTPS

HTTP method: GET



![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/dc56f68d-8daf-4b31-bc04-5bd2547ffac9/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46663I3I45Z%2F20260110%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260110T011658Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIGAywAAt%2BapN0dpKJ53WHmVCCp1%2BGwQhfF23N3tLDtqDAiEAlJqAIz3w0ypLBk%2FBVqeYC75DurKW4G%2BYX2o3Yb1xebEqiAQIsv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDEnveQjlbJUtJf3ZDSrcA%2BfYOwUfzOFKNHtQpCXqk2QqtsD24Gx16VTfD5yV4FxGDElU7UWCqtcckeVqxzS%2BDlRS037DBqceg%2Bw3c%2F%2BMltdkPHOu4jdsNBE1hN6lLxz3Bpj96yvt%2BAcXwLsAZOPbMN9uWMFuKE%2F2u94xHUHeaRup7ZFM49DLgcmVmp%2BLVpXTCDj8pwQHqQQaZgdXUe%2FZPc5dkznkYJ2%2FfPlXRVOnVqI8HCEejDaQ%2B1QTUhAj1i6kom8sNpMOmwECjY05VkuJIOeIKi5I5w9MUWRw8EKaRbo7gWgVi%2BjkgGXnYkSbOyTHkF5EZTKTmZlShrajJFnulRFh6eL6lyofK9mEMG4oa2Enw1wNm%2Bime4szeAMyYJoTGySkRhLQafOzLt1LSGucbwSJ0ahmyHUArp96sgMzn4jSSFIYWXPERjw8y1xWIBuB6Qb9IRSWWEh8DYF7G4iTXNxPbG%2FFpRpxbByOxMfVfOUBjH4%2B52ubU%2BEV3TAOd3kHY%2F2JmfZfWK%2B0jgafEa8c51xFDy66SijVsViEaWzl%2BaFjQeG5zRF7cMm2kuHKV5jacpKrIMgkOsVA2HWVkUhiQhtGzSIv5yTpQV%2BKlA44sfuZ4Cb6hyQ6CkqAYRhhXUHFefV9Mlf6D8vxeJFRMNLAhssGOqUBJ8L5g8GPtSy11HW%2BWhBRpzXkX9GQ73I343lJEPNVYAoFDNycmNWMHR1q7ppy16G2RGXksMsmT20s6QThkFIc%2FDpGfuxBl78%2FQYKLhJEzX9jiibaZEG3c0LeMwy%2BtsqVCQOBBGo7FFgm6UlvbpsKX7faywLKiycGa9wXcjphRXHvwJWVlDlkuKQv9zcKWk9QHViJcO5h2RHn5YI6yy6L2qIgnpmoz&X-Amz-Signature=2fe699d453dafc2eda5cb8746ea1c014828d8060c5a3df4b43bdcb7d18a34396&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)





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







