import numpy as np
import pandas as pd
import random

def generate_synthetic_beam_data(num_samples=300, random_seed=42):
    """
    Generates a synthetic dataset for beam load-deflection analysis.
    
    Columns:
        L (m) - Span length
        b (m) - Beam width
        h (m) - Beam height
        E (GPa) - Modulus of Elasticity
        Reinf (ratio) - Steel ratio or 0 for none
        BC - Boundary condition (simply supported or fixed)
        P (kN) - Applied load
        δ_max (mm) - Maximum deflection
        P_u (kN) - Ultimate load capacity
        FoS - Factor of safety (P_u / P)
        w_cr (mm) - Crack width
    """
    np.random.seed(random_seed)
    random.seed(random_seed)

    # Number of samples
    n = num_samples

    # 1. Generate input variables
    # ------------------------------------------------
    
    # Span length (L): uniform between 2m and 8m
    L = np.random.uniform(low=2.0, high=8.0, size=n)
    
    # Cross-section dimensions:
    #   b in [0.2, 0.5] m
    #   h in [0.3, 1.0] m
    b = np.random.uniform(low=0.2, high=0.5, size=n)
    h = np.random.uniform(low=0.3, high=1.0, size=n)
    
    # Modulus of Elasticity E in [20, 35] GPa
    E = np.random.uniform(low=20.0, high=35.0, size=n)
    
    # Reinforcement ratio in [0, 0.04]
    # We'll interpret 0 as 'no reinforcement'
    Reinf = np.random.uniform(low=0.0, high=0.04, size=n)
    
    # Boundary conditions: "SS" or "FIXED"
    # We'll pick randomly between these two
    BC_choices = ["SS", "FIXED"]
    BC = [random.choice(BC_choices) for _ in range(n)]
    
    # Applied load (P) in [50, 200] kN
    P = np.random.uniform(low=50, high=200, size=n)
    
    # 2. Compute derived geometry/material properties
    # ------------------------------------------------
    
    # Convert E from [GPa] to [kN/m^2] for consistency
    # 1 GPa = 1e9 N/m^2 = 1e3 kN/m^2
    E_kNm2 = E * 1e3  # now in kN/m^2
    
    # Moment of inertia I for rectangular cross-section: I = b * h^3 / 12
    # We'll keep b,h in [m], so I is in [m^4]
    I = (b * (h**3)) / 12.0
    
    # 3. Calculate output variables
    # ------------------------------------------------
    # For maximum deflection, we’ll use a simple formula for a single mid-span load:
    #   δ_max = (P * L^3) / (48 * E * I) for a simply supported beam
    # If BC is "FIXED", we'll reduce deflection by a factor (like ~1/4 or 1/2).
    
    delta_max = []
    for i in range(n):
        # Convert P (kN) => N by multiplying 1e3, but let's stay consistent in our chosen system
        # We'll do a simplified approach: Keep P in kN, E in kN/m^2, I in m^4, L in m
        # Then we must handle units carefully so the final deflection is in mm.
        
        # We'll define a numeric factor for the simply supported deflection formula in consistent units:
        #   δ [m] = (P [kN]*1e3 N/kN * L^3 [m^3]) / (48 * E [kN/m^2]*1e3 N/kN * I [m^4])
        # For simplicity, let's skip a detailed unit check and just do a ratio that yields a plausible outcome in meters,
        # then convert to mm. We'll also incorporate some random noise.
        
        # Basic formula factor for a simply supported beam with a single point load at midspan:
        #   δ = (P * L^3) / (48 * E * I)
        # We might scale things to get a range in a plausible deflection region.
        
        factor = (P[i] * (L[i]**3)) / (48.0 * E_kNm2[i] * I[i])
        
        # If the beam is fixed, deflection is typically smaller. Let's reduce it further:
        if BC[i] == "FIXED":
            factor *= 0.3  # e.g., an approximate ratio compared to simply supported
        
        # Convert factor from [m] to [mm] with a scale factor guess that ensures deflections are not too large
        # We'll scale up or down to get realistic deflection magnitudes
        # We'll multiply by 1e3 to convert to mm, and add some random variation
        base_deflection = factor * 1e3  # now in mm
        # Add small random noise (±10%)
        noise = base_deflection * (0.1 * np.random.uniform(-1, 1))
        d = base_deflection + noise
        
        # Ensure deflection is non-negative (just in case)
        d = max(0.0, d)
        delta_max.append(d)
    
    # 4. Ultimate load capacity (P_u)
    # ------------------------------------------------
    # We'll define a simplified relationship:
    #   P_u ~ alpha * (E * I / L^2) + beta * (Reinf) * (b * h)
    # plus some random scatter
    # alpha, beta are constants chosen to produce plausible values.
    
    alpha = 2.0e2  # tune to produce load in range of 200-1000 kN
    beta = 5.0e4   # tune to reflect effect of reinforcement
    # We'll do a small factor for boundary condition too:
    # If fixed, let's assume it can carry more load
    P_u = []
    for i in range(n):
        bc_factor = 1.2 if BC[i] == "FIXED" else 1.0
        # E_kNm2[i]*I[i] / (L[i]^2) has units ~ kN? We'll scale with alpha
        base_pu = alpha * (E_kNm2[i]*I[i]) / (L[i]**2)
        # Add effect of reinforcement (assume Reinf is up to 0.04 => up to 4% steel)
        base_pu += beta * Reinf[i] * (b[i]*h[i])
        # Multiply by bc_factor and random noise ±10%
        load_val = base_pu * bc_factor
        load_val += load_val * (0.1 * np.random.uniform(-1,1))
        load_val = max(load_val, 0.0)
        P_u.append(load_val)
    
    # 5. Factor of Safety (FoS) = P_u / P
    # ------------------------------------------------
    FoS = [P_u[i] / P[i] for i in range(n)]
    
    # 6. Crack width (w_cr) [only if Reinf>0, else 0]
    # ------------------------------------------------
    # We'll define a simple approach: w_cr ~ gamma * (P/P_u) * Reinf * h
    # where gamma is a constant. We'll add random scatter.
    
    gamma = 0.5  # scaling constant
    w_cr = []
    for i in range(n):
        if Reinf[i] > 0.0:
            ratio = P[i]/(P_u[i] + 1e-6)  # avoid div-by-zero
            base_w = gamma * ratio * Reinf[i] * h[i] * 1e3  # in mm
            base_w += base_w * (0.1 * np.random.uniform(-1,1))  # ±10% noise
            base_w = max(base_w, 0.0)
            w_cr.append(base_w)
        else:
            w_cr.append(0.0)

    # 7. Beam type (concrete, steel, prestressed, wood)
    # ------------------------------------------------
    beam_type_choices = ["concrete", "steel", "prestressed_concrete", "wood"]
    beam_type = random.choices(
        population=beam_type_choices,
        weights=[0.4, 0.3, 0.2, 0.1],  # adjust weights as desired
        k=n
    )
    # 8. Build the dataset as a pandas DataFrame
    # ------------------------------------------------
    data = {
        "span_length_m": L,
        "beam_width_m": b,
        "beam_height_m": h,
        "modulus_of_elasticity_gpa": E,
        "reinforcement_ratio": Reinf,
        "boundary_condition": BC,
        "applied_load_kn": P,
        "max_deflection_mm": delta_max,
        "ultimate_load_kn": P_u,
        "factor_of_safety": FoS,
        "crack_width_mm": w_cr,
        "beam_type": beam_type
    }
    
    df = pd.DataFrame(data)
    return df


def main():
    # Generate the synthetic dataset
    df_beams = generate_synthetic_beam_data(num_samples=200, random_seed=42)
    
    # Save to CSV
    df_beams.to_csv("synthetic_beam_data.csv", index=False)
    print("Synthetic beam dataset saved to 'synthetic_beam_data.csv'.")
    
    # (Optional) Quick preview
    print(df_beams.head(10))


if __name__ == "__main__":
    main()
