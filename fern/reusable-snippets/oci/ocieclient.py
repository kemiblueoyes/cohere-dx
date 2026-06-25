import cohere

co = cohere.OciClient(
    oci_region="us-chicago-1",
    oci_compartment_id="ocid1.compartment.oc1...",
)