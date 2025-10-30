



ODATA —> Open Data Protocol 







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


- Message body
-  Header


![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/de3257b0-99da-4a97-9108-71d731170890/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662JUCTQ25%2F20251030%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251030T225437Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjED4aCXVzLXdlc3QtMiJIMEYCIQDziH%2FeZxv6ytvZD4J5%2BI9RXI8GpVqo6Uoe2%2BrtQ1hI%2FwIhAMO2o9lAwXkAO3aq1Jn%2BDJbrFG0HXyalosUpmKhhsEH5KogECPf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igz9cd0kTZWqdG5DODgq3AMUVhRua5Hdoaa6f2GoguwqMRa9yWvl6EaRA5esRBA8EyiKMNdZ6w09tdZx%2BFZhPAbzxfxKhzoTHSA9Be%2BIOcWBv7fCIyU4CNdWJ6oaq%2BEH32COQxSdAt3OnnhE80udS4ZJnvwB%2FaxnVaCnwugE0Oz%2BANoRebn4TkNQHX3gXtEAaLm%2FHmXPNJHmp9w5GacTWr3sbh1SHadrBZkcibTGBZUhaPeoQR34cfzirarg9ZP6PPd5KmuTw2r1wFDg65pyjQCP40Ln3Cj5gQyGYLw3vHO6y741TfKWsbL3%2FOj3nLa5f4VvA8R%2BwccVmy36pHDm7zaKRMUuaXDoeGQ%2F1sqIeCLSaBTiIP%2FM3DRTBk78d5eoAlNukoLRb%2BQUveQESLVPCf1mr2AfGFAvmJZI7UPh3axWMNwNoJA%2F7nAX0NvYTvwdJA9od0by69amLS%2FJP63nLbB82R2z1AEz6k1xoOWLaI9NryjNriqu5O1RH4nhoUJ90wWrlXQKK7RmsGh2e2LfimfXAtFV0it2GGGxuuwrYO31snwluYLGJxiLy1uP8OhYJ4YFvJZqE3mU0%2FZOgq84SBOc7cnl5KWBv6%2BLbGrXObMe0p97r0jEqdvsvKRfQCTRb2rmp2IK7C72tMGXyTCyxo%2FIBjqkAXVM7Frbo4Y8GSe3nsWuUoOHg%2FrdoYjgJ8F1VN8xLV1zgvJQR1XHf09TyPzLapVqufcZ3JZ%2BXne%2FgTlbPK7Tj3k3%2FobXVE6pg0j9izhLxD6R0DN4BeTVW%2BhRfqOmvxW1Gqe8gpzuBHFzuFgMsyFqYCG9qW2rxrmJQBUz7pvcZkFRcdqgCI64F4CJLF9TI%2B73YxfHZUr%2F9IsPszhXmOyJ%2FB5nh8q9&X-Amz-Signature=be5e29c7a06fdb42ef53ee260b4dcba1a9e91467607df120f32e7153cafe0687&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



Port 443: HTTPS

HTTP method: GET



![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/dc56f68d-8daf-4b31-bc04-5bd2547ffac9/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662JUCTQ25%2F20251030%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251030T225438Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjED4aCXVzLXdlc3QtMiJIMEYCIQDziH%2FeZxv6ytvZD4J5%2BI9RXI8GpVqo6Uoe2%2BrtQ1hI%2FwIhAMO2o9lAwXkAO3aq1Jn%2BDJbrFG0HXyalosUpmKhhsEH5KogECPf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igz9cd0kTZWqdG5DODgq3AMUVhRua5Hdoaa6f2GoguwqMRa9yWvl6EaRA5esRBA8EyiKMNdZ6w09tdZx%2BFZhPAbzxfxKhzoTHSA9Be%2BIOcWBv7fCIyU4CNdWJ6oaq%2BEH32COQxSdAt3OnnhE80udS4ZJnvwB%2FaxnVaCnwugE0Oz%2BANoRebn4TkNQHX3gXtEAaLm%2FHmXPNJHmp9w5GacTWr3sbh1SHadrBZkcibTGBZUhaPeoQR34cfzirarg9ZP6PPd5KmuTw2r1wFDg65pyjQCP40Ln3Cj5gQyGYLw3vHO6y741TfKWsbL3%2FOj3nLa5f4VvA8R%2BwccVmy36pHDm7zaKRMUuaXDoeGQ%2F1sqIeCLSaBTiIP%2FM3DRTBk78d5eoAlNukoLRb%2BQUveQESLVPCf1mr2AfGFAvmJZI7UPh3axWMNwNoJA%2F7nAX0NvYTvwdJA9od0by69amLS%2FJP63nLbB82R2z1AEz6k1xoOWLaI9NryjNriqu5O1RH4nhoUJ90wWrlXQKK7RmsGh2e2LfimfXAtFV0it2GGGxuuwrYO31snwluYLGJxiLy1uP8OhYJ4YFvJZqE3mU0%2FZOgq84SBOc7cnl5KWBv6%2BLbGrXObMe0p97r0jEqdvsvKRfQCTRb2rmp2IK7C72tMGXyTCyxo%2FIBjqkAXVM7Frbo4Y8GSe3nsWuUoOHg%2FrdoYjgJ8F1VN8xLV1zgvJQR1XHf09TyPzLapVqufcZ3JZ%2BXne%2FgTlbPK7Tj3k3%2FobXVE6pg0j9izhLxD6R0DN4BeTVW%2BhRfqOmvxW1Gqe8gpzuBHFzuFgMsyFqYCG9qW2rxrmJQBUz7pvcZkFRcdqgCI64F4CJLF9TI%2B73YxfHZUr%2F9IsPszhXmOyJ%2FB5nh8q9&X-Amz-Signature=5c6a4c69f8f00c9409725a0ae3a128b94729abde107820ecbea0bf040393c53e&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)





For HTTP PORT is 80



What is ODATA?

Applying and building on Web technologies such as



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





Test Github-Notion synch



