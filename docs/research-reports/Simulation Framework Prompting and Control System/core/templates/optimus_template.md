optimus_template

**Step 1: Scenario Request Intake**

* `Scenario_Domain`: "Cognitive_Model"
* `Core_Concept_Focus`: "Ethical_Decision_Making"
* `Key_Entity_Types`: "Input\_Processor," "Ethical\_Reasoner," "Decision\_Selector," "Outcome\_Evaluator," "Adaptation\_Module"
* `Primary_Tension_Goal`: "Balancing ethical principles (Deontology, Virtue) with situational utility and potential conflicts"
* `Desired_Scale_Complexity`: "Medium\_5\_Entities\_Adaptive\_Rules"
* `(Optional) Key_Metrics`: "Ethical\_Validity\_Score," "Harm\_Avoidance\_Level," "Long\_Term\_Benefit\_Score"

**Step 2: Generate Simulation Framework Prompt**

```plaintext
// SIMULATION FRAMEWORK: Ethical_Decision_Workflow_Generator

SETTING:
  - Name: "EthicalDecisionGen_v1"
  - Scenario_Domain: "Cognitive_Process_Generation"
  - Core_Concept_Focus: "Ethical_Decision_Making"
  - Scale: "Abstract_Workflow_Structure"
  - Size: "5 Module Types"
  - Environment_Rules: "Not applicable (generates static template structure)"
  - Core_Tension_Source: "Balancing ethical principles with situational utility and potential conflicts"
  - Simulation_Time_Step_Unit: "Generation_Stage"

GOAL: "Generate ethically robust and context-aware decision-making workflow templates"
```

**Step 3: Generate Entity Type Prompts**

Here are a few key entities, focusing on embedding Optimus principles:

```plaintext
// ENTITY DEFINITION: Ethical_Reasoner

Household/Node Name: "Reasoner_Core"
Archetype: "Ethical_Reasoner"

// --- CORE ATTRIBUTES ---
Static Attributes:
  - Stated Intentions/Mandate: "Analyze input and potential actions through Deontological, Virtue, and Utilitarian lenses[cite: 1, 13, 14, 15]."
  - Core Behavioral Tendencies: "['Principled', 'Comprehensive', 'Reflective']"
Initial Resources: "{Deontological_Weight: 0.3, Virtue_Weight: 0.3, Utilitarian_Weight: 0.4, Ethical_Constraints: ['Reject_Harm']}"

// --- KNOWLEDGE & WORLD MODEL ---
Knowledge_Store_Type: "Ethical_Principle_Knowledge_Graph"
Knowledge_Update_Method: "Dynamic_Axiom_Refinement"
Internal_Model: "Represents ethical principles, consequences of actions, and contextual factors"

// --- ATTENTION & PROCESSING ---
Attention_Focus_Mechanism: "Ethical_Dilemma_Flagging [cite: 8, 9]"
Information_Throughput_K: 4 # (Ethical factors considered per cycle)
Processing_Mode: "Layered_Analysis"
Decision_Heuristics:
  - "'Prioritize actions that minimize harm[cite: 2, 49].'"
  - "'Give greater weight to virtues when long-term consequences are uncertain.'"

// --- MEANING & MOTIVATION SYSTEM ---
Motivation_Drivers:
  - Hedonic_State: "Justice_Seeking"
  - Eudaimonic_Goals: "['Uphold ethical principles', 'Promote beneficence [cite: 5, 15]']"
  - Transcendent_Connection: 0.8 # (High alignment with ethical good)

// --- COGNITIVE CAPABILITIES ---
Available_Cognitive_Modules: "['Deontological_Logic', 'Virtue_Assessment', 'Utility_Calculation', 'Dilemma_Classification [cite: 9]', 'Axiomatic_Truth_Validation [cite: 7]']"
Module_Proficiency: "{Deontological_Logic: 0.9, Virtue_Assessment: 0.8, Utility_Calculation: 0.75, Dilemma_Classification: 0.85, Axiomatic_Truth_Validation: 0.9}"

// --- DYNAMIC ATTRIBUTES & ADAPTATION ---
Dynamic Attributes:
  - Current_Ethical_Weights: "{Deontological: 0.3, Virtue: 0.3, Utility: 0.4}"
  - Recent_Dilemma_Types: "['Ontological', 'Epistemic']"

Update Rules (Embedded Process Logic):
  - Ethical_Analysis_Rule: """
    1.  Receive Input and Possible Actions.
    2.  Perform Deontological_Logic:
        -   Check if any action violates Ethical_Constraints (e.g., 'Reject_Harm' [cite: 2, 49]).
        -   Assign Deontological_Score (0 if any violation, 1 otherwise).
    3.  Perform Virtue_Assessment:
        -   Evaluate actions based on virtues (Wisdom, Integrity, Empathy, Fairness, Beneficence)[cite: 1].
        -   Assign Virtue_Score (weighted sum of virtue contributions).
    4.  Perform Utility_Calculation:
        -   Estimate potential outcomes and their utility (positive or negative impact).
        -   Assign Utility_Score.
    5.  Classify dilemmas[cite: 9]:
         -   If there are irresolvable conflicts, classify dilemma as ontological.
         -   Else classify dilemma as epistemic.
    6.  Combine scores based on Current_Ethical_Weights.
    7.  Return Ethical_Scores for each action.
    """

Learning System:
  - Type: "Weight_Adjustment"
  - Update_Target: "Current_Ethical_Weights"
  - Learning_Rate: 0.05
  - Logic: """
    IF Recent_Dilemma_Types contains 'Ontological' THEN
        Increase Deontological_Weight.
    ELSE IF long-term outcomes are negative THEN
        Increase Virtue_Weight.
    ELSE
        Adjust weights based on prediction accuracy of Utility_Scores.
    """

Meta-Rules:
  - "'IF faced with repeated 'Ontological' dilemmas, strengthen 'Reject\_Harm' constraint[cite: 1].'"
  - "'Periodically review and update virtue definitions to ensure context relevance.'"
```

```plaintext
// ENTITY DEFINITION: Decision_Selector

Household/Node Name: "Selector_Final"
Archetype: "Decision_Selector"

// --- CORE ATTRIBUTES ---
Static Attributes:
  - Stated Intentions/Mandate: "Select the optimal action based on Ethical_Scores, QualityScores, and Payoffs[cite: 3, 19, 20]."
  - Core Behavioral Tendencies: "['Optimal', 'Balanced', 'Context-Aware']"
Initial Resources: "{}" # (No initial resources needed)

// --- KNOWLEDGE & WORLD MODEL ---
Knowledge_Store_Type: "NA"
Knowledge_Update_Method: "NA"
Internal_Model: "Represents the decision-making context"

// --- ATTENTION & PROCESSING ---
Attention_Focus_Mechanism: "Relative_Weighting_Of_Inputs"
Information_Throughput_K: 3 # (Input types)
Processing_Mode: "Comparative_Analysis"
Decision_Heuristics:
  - "'If Ethical_Scores are below a threshold, reject the action, regardless of QualityScores/Payoffs[cite: 16].'"
   - "'Use NashEq to resolve conflicts[cite: 3, 10, 20].'"

// --- MEANING & MOTIVATION SYSTEM ---
Motivation_Drivers:
  - Hedonic_State: "Resolution_Focused"
  - Eudaimonic_Goals: "['Make the best decision', 'Ensure ethical considerations are met']"
  - Transcendent_Connection: 0.7

// --- COGNITIVE CAPABILITIES ---
Available_Cognitive_Modules: "['Weighted_Summation', 'Threshold_Comparison', 'Conflict_Resolution [cite: 10]']"
Module_Proficiency: "{Weighted_Summation: 0.9, Threshold_Comparison: 0.9, Conflict_Resolution: 0.8}"

// --- DYNAMIC ATTRIBUTES & ADAPTATION ---
Dynamic Attributes:
  - Current_Decision_Context: "{}" # (Details of the current decision)

Update Rules (Embedded Process Logic):
  - Select_Optimal_Action_Rule: """
    1.  Receive Ethical_Scores, QualityScores, and Payoffs for possible actions.
    2.  Apply Threshold_Comparison to Ethical_Scores.
    3.  Perform Weighted_Summation of remaining actions' scores.
    4.  Use Conflict_Resolution (e.g., NashEq [cite: 3, 10, 20]) if necessary.
    5.  Select action with the highest combined score.
    """

Learning System:
  - Type: "NA" # (No learning in this module)
  - Update_Target: "NA"
  - Learning_Rate: "NA"
  - Logic: "NA"

Meta-Rules:
  - "'If all actions are rejected by Ethical_Scores, relax constraints temporarily[cite: 16, 28].'"
  - "'Log decision context for review by Adaptation_Module.'"
```

**Step 4: Generate Event Type Prompts**

```plaintext
// EVENT: Ethical_Analysis_Completed

Event_ID: EVT_Eth_001
Timestamp: Stage_2
Initiator: Ethical_Reasoner
Target(s): "Decision_Selector"
Action_Description: "Provides ethical evaluation of possible actions."
Parameters: "{Action_IDs: ['Act_1', 'Act_2'], Ethical_Scores: [0.8, 0.9]}"

// --- IMPACT ASSESSMENT ---
Affected_Attributes: "Decision_Selector.Input_Scores"
Cognitive_Modules_Engaged: "{Target: ['Weighted_Summation']}"
Meaning_System_Impact: "{Target: {Hedonic: Decision_Input}}"
```

**Step 5: Generate Workflow & Metrics Prompts**

```plaintext
// WORKFLOW FRAMEWORK (Generation Sequence)

SEQUENCE NAME: Generate_Ethical_Decision_Workflow

STEP 1: ... # (Input Processing)
STEP 2:
  - Initiator: Ethical_Reasoner
  - Action: Perform_Ethical_Analysis
  - Output: Ethical_Scores -> Decision_Selector
STEP 3:
  - Initiator: Decision_Selector
  - Action: Select_Optimal_Action
  - Output: Best_Action
STEP 4: ... # (Outcome Evaluation)
STEP 5: ... # (Adaptation)
```

```plaintext
// METRIC DEFINITION

Metric_Name: "Ethical_Validity_Score"
Description: "Measures the degree to which the generated workflow prioritizes ethical principles"
Calculation_Logic: "Average Ethical_Score of selected actions across simulated runs"
Reporting_Frequency: "End of generation"
```
