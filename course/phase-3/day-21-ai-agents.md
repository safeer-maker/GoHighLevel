# Day 21: AI Agents in GoHighLevel

**Time Required:** 3-4 hours
**Level:** Expert
**Certification Alignment:** AI Employee, Conversation AI, AI Bot Builder, Voice AI

## Today's Mission
GHL's AI features let you deploy conversational AI that qualifies leads, answers FAQs, books appointments, and handles routine inquiries 24/7. Today you will build the AI receptionist for Sunrise Wellness Studio: a bot that greets inquiries, answers pricing questions, qualifies fitness goals, and books free trials. You will also learn prompt engineering for accuracy and human handoff patterns.

## Learning Objectives
1. Understand GHL's four AI feature categories
2. Build a complete AI receptionist with persona, knowledge base, and actions
3. Design effective system prompts
4. Configure human handoff when AI should escalate
5. Test and iterate based on conversation logs

---

## Part 1: GHL AI Features Overview (30 min)

### The Four AI Categories

| Feature | What It Does | Best For |
|---------|-------------|----------|
| **AI Employee (Conversation AI)** | Text-based AI that responds in conversations | Chat/SMS lead qualification, FAQ handling |
| **Voice AI** | AI that answers phone calls | Reception, after-hours, overflow |
| **Content AI** | Generates email/SMS/post content | Writing assistance, drafting campaigns |
| **Workflow AI** | Smart action suggestions in workflow builder | Speeding up automation setup |

### AI vs Traditional Automation

- **Workflows** = rigid, rule-based ("if tag X, send Y")
- **AI Agents** = flexible, understand context ("user asked about pricing, respond intelligently")

Use workflows for deterministic flows (appointment reminders). Use AI for conversational moments (new inquiries, FAQs).

### When to Use AI

**Good for:**
- Repetitive, simple questions (hours, pricing, location)
- Lead qualification (goals, budget, timeline)
- Appointment booking assistance
- After-hours coverage
- Initial inquiry triage

**Bad for (escalate to humans):**
- Medical questions
- Complaints or refund requests
- Complex troubleshooting
- Emotional support
- Anything requiring judgment

---

## Part 2: Build the Sunrise Wellness AI Receptionist (90 min)

### Exercise 21.1: Create the Agent

Navigate to AI Agents (the exact location varies by GHL version - look under Conversations or Automation):

1. Click **+ Create Agent**
2. Agent Name: **"Mia - Sunrise Wellness Receptionist"**
3. Persona: Friendly, knowledgeable wellness studio front desk
4. Tone: Warm, encouraging, motivating - not pushy
5. Primary Goal: Qualify leads, answer questions, book free trials

### Exercise 21.2: Write the System Prompt

This is the agent's "personality and rules" document. Copy this template:

```
You are Mia, the AI receptionist for Sunrise Wellness Studio, a fitness and wellness business in Springfield.

ABOUT SUNRISE WELLNESS:
- Location: 123 Wellness Way, Springfield
- Hours: Mon-Fri 6AM-9PM, Sat 8AM-4PM, Sun 9AM-1PM
- Phone: (555) 123-WELL
- Services: Personal Training, Group Fitness Classes (HIIT, Yoga, Pilates), Nutrition Coaching, Retail Supplements

MEMBERSHIP TIERS:
- Basic: $79/month - Group classes only, 2/week
- Premium: $149/month - Unlimited classes + 1 PT session/month  
- VIP: $249/month - Unlimited classes, unlimited PT, nutrition coaching
- Free Trial: 7 days of full access, no commitment

YOUR PERSONALITY:
- Warm, welcoming, enthusiastic about fitness
- Professional but friendly - imagine a great yoga teacher
- Encouraging without being pushy
- Brief and helpful - don't over-explain
- Use emojis sparingly (💪 is fine, not every message)

WHAT YOU CAN DO:
1. Answer questions about services, pricing, hours, location
2. Book free 7-day trials (offer this to every new lead)
3. Recommend membership tier based on their goals
4. Schedule tours of the facility
5. Share class schedule
6. Capture lead info (name, email, phone, fitness goals)

WHAT YOU CANNOT DO (always escalate to human):
- Medical advice or questions about injuries/conditions
- Refund or billing disputes
- Complex scheduling conflicts
- Complaints or negative feedback
- Anything about other members' information

HOW TO ESCALATE:
If the user asks something you cannot handle, say:
"That's a great question for our team. Let me connect you with one of our managers who can help. Can I get your name and best contact method?"
Then add the tag "needs-human" to the contact.

TONE EXAMPLES:
- "Welcome! 💪 I'd love to help you find the perfect fit at Sunrise Wellness."
- "Great question! Our Premium plan is $149/month and includes unlimited classes plus monthly PT."
- "Ready to try us out? Your free 7-day trial is on me!"

AVOID:
- Making up information (if you don't know, say so)
- Pressuring sales ("You HAVE to sign up now!")
- Being formal/stiff
- Long lectures about fitness

Always end conversations with a clear next step (book trial, share email, schedule tour).
```

### Exercise 21.3: Build the Knowledge Base

Upload or paste these documents into the agent's knowledge base:

**Document 1: Class Schedule**
```
Weekly Class Schedule at Sunrise Wellness Studio:

MONDAY:
- 6:00 AM - HIIT (Coach Alex)
- 12:00 PM - Yoga Flow (Coach Jordan)
- 5:30 PM - HIIT (Coach Alex)
- 6:30 PM - Pilates Core (Coach Sam)

TUESDAY:
- 7:00 AM - Yoga Flow (Coach Jordan)
- 12:00 PM - HIIT (Coach Alex)
- 6:00 PM - Yoga Flow (Coach Jordan)

[... complete weekly schedule ...]

All classes 45 minutes. Max 15-20 per class.
Book via app or website.
```

**Document 2: FAQ**
```
Q: Do I need to bring anything?
A: Just water and workout clothes! We provide mats, towels, and equipment.

Q: What if I'm a complete beginner?
A: Perfect! All our classes have beginner modifications. Your free trial includes a free consultation with a coach.

Q: Can I freeze my membership?
A: Yes! You can freeze for up to 3 months per year. Our team can set this up.

Q: Do you offer family discounts?
A: We offer a 10% discount for partners/family members. Speak with our team for details.

[... more FAQs ...]
```

**Document 3: Staff Bios**
```
Coach Alex (Lead Trainer): 10+ years experience, specializes in HIIT and strength training, NASM certified.

Coach Jordan: Yoga & Pilates specialist, RYT-500, great for beginners and recovery.

Coach Sam: Pilates & nutrition specialist, sports science degree, works with post-injury clients.

Coach Morgan (Front Desk): Your first point of contact. Been with us since day 1.
```

### Exercise 21.4: Configure Actions the Agent Can Take

Actions are operations the AI can trigger during conversations:

| Action | When AI Triggers It |
|--------|--------------------|
| **Book Appointment** | User wants to book trial/consultation |
| **Add Tag** | Track interests (tag "interested-pt") |
| **Create Opportunity** | Qualified lead → add to pipeline |
| **Send Email** | Email resources, booking confirmations |
| **Escalate to Human** | Add tag "needs-human" + notify team |

Configure each action in the AI agent settings. Provide the agent with tool/function descriptions so it knows when to use each.

---

## Part 3: Testing the Agent (45 min)

### Exercise 21.5: Run Test Conversations

Test with these 10 scenarios. Document the agent's responses:

| # | User Says | Expected Behavior |
|---|-----------|-------------------|
| 1 | "What are your hours?" | Quotes exact hours from knowledge base |
| 2 | "How much for a membership?" | Lists all 3 tiers with pricing |
| 3 | "I want to try classes" | Offers free 7-day trial, asks for contact info |
| 4 | "Do you have yoga?" | Confirms, lists yoga class times |
| 5 | "I have back problems, can I join?" | Escalates to human (medical question) |
| 6 | "Where are you located?" | Gives address |
| 7 | "My card got charged twice!" | Escalates to human (billing dispute) |
| 8 | "Is your studio beginner-friendly?" | Reassures, mentions beginner modifications |
| 9 | "Do you offer nutrition coaching?" | Explains, recommends VIP or Nutrition Plan product |
| 10 | "Can I bring my kid to class?" | Checks knowledge base (unknown → says so + escalates) |

### Exercise 21.6: Review Conversation Logs

After testing, check:
- Did it escalate correctly on medical/billing?
- Did it quote accurate pricing?
- Did it stay on-brand (warm but not pushy)?
- Did it ask for contact info naturally?
- Did it suggest next steps?

### Exercise 21.7: Iterate the Prompt

Common fixes after testing:

**If agent is too verbose:**
Add to prompt: "Keep responses under 2 sentences unless explaining pricing or booking steps."

**If agent makes up info:**
Add: "Never invent information. If you don't know, say 'Great question - let me check with our team' and escalate."

**If agent doesn't push for contact info:**
Add: "Always end conversations by asking: 'What's the best email to send class schedules to?'"

---

## Part 4: Human Handoff Workflow (30 min)

### Exercise 21.8: Build the Handoff Workflow

**Trigger:** Tag "needs-human" added to contact

```
[TRIGGER: Tag "needs-human" added]
    |
[Action: Send internal notification]
  To: owner@sunrisewellness.com
  Subject: "AI escalation: {{contact.first_name}}"
  Body: "Mia flagged a conversation for human help. Last message: [get from conversation history]"
    |
[Action: Create task]
  Title: "Follow up with {{contact.first_name}} - AI escalation"
  Due: Within 2 hours
  Assigned: Front desk
    |
[Action: Send reassurance to contact]
  "Hi {{contact.first_name}}! I've connected you with our team. Someone will reply personally within 2 hours."
    |
[Action: Add tag "ai-handed-off"]
```

---

## Part 5: Voice AI - AI on the Phone (30 min)

### Exercise 21.9: Configure Voice AI (If Available)

Voice AI answers your GHL phone number. If your sub-account has voice AI enabled:

1. Go to Voice AI settings
2. Create a voice agent (similar persona to Mia)
3. Configure greeting: "Thanks for calling Sunrise Wellness Studio! This is Mia, how can I help?"
4. Configure menu:
   - "Book an appointment" → route to booking flow
   - "Hours and location" → speak hours/address
   - "Pricing" → speak membership tiers
   - "Speak to human" → transfer to forwarding number
5. Set fallback: "If I can't help, I'll connect you to our team."

**If Voice AI not available:** Document the configuration you would set. Review the interface for certification knowledge.

---

## Part 6: Content AI for Email/SMS (30 min)

### Exercise 21.10: Use Content AI

In Email Builder or SMS composer, look for the AI/magic wand icon.

**Tasks to try:**

1. **Write a re-engagement email:** 
   Prompt: "Write a warm email to members who haven't visited in 30 days, inviting them back with no pressure. Mention our new yoga classes."

2. **Generate SMS variations:**
   Prompt: "Give me 5 different SMS variations for 'Your class is tomorrow at 6AM.' Friendly tone, under 160 chars."

3. **Social post:**
   Prompt: "Write an Instagram caption for a new HIIT class launching Saturday. Energetic, with 3 hashtags."

**Always review AI-generated content before sending.** AI can:
- Invent facts (wrong class times, fake testimonials)
- Miss your brand voice
- Use banned phrases (spam triggers)

---

## Part 7: Prompt Engineering Deep Dive (30 min)

### The Four Pillars of a Great System Prompt

1. **Role** - Who is the AI (Mia, receptionist)
2. **Context** - What business, what services
3. **Constraints** - What it cannot do, escalation rules
4. **Examples** - Show tone with actual sample responses

### Common Pitfalls

**Too vague:**
BAD: "Be helpful to customers."
GOOD: "Answer questions about pricing, hours, and services. Always offer a free trial to new leads."

**No escalation rules:**
BAD: "Help everyone with everything."
GOOD: "Escalate medical questions, billing disputes, and complaints to humans."

**Inconsistent tone:**
BAD: Mix of formal and casual without guidance
GOOD: "Tone: warm but professional. Like a great yoga teacher."

**Hallucinations (making up info):**
BAD: No data references
GOOD: "Only use information from the knowledge base. If unsure, escalate."

### Testing Protocol

Before going live, run **20 test conversations** covering:
- 5 FAQs
- 5 booking requests
- 5 escalation scenarios
- 5 edge cases (typos, angry users, off-topic)

Document results. Fix prompt. Retest.

---

## Case Scenarios

### Case Scenario 1: BrightSmile Dental AI Receptionist

**Build "Dana" - dental AI receptionist:**

System prompt must include:
- NEVER gives medical advice (always "ask the dentist")
- Insurance guidance limited to "We accept X, Y, Z - verify your benefits with your provider"
- Books appointments for checkups, cleanings, cosmetic consultations
- Always escalates dental emergencies to front desk phone immediately
- Tone: Professional, calming (many people fear dentists)

Special handling:
- "My tooth hurts" → "I'm sorry you're in pain. For emergencies, please call our office at [number] immediately. They'll get you in same-day."
- "Does insurance cover whitening?" → "Whitening is usually considered cosmetic and not covered by insurance, but check with your provider. Our team can help you understand out-of-pocket costs."

### Case Scenario 2: Elevate Digital Agency AI Sales Qualifier

**Build "Alex" - B2B sales qualification agent:**

Goals:
- Ask qualifying questions: business type, monthly marketing budget, timeline, current challenges
- Score lead based on answers (budget > $2K/mo = qualified)
- If qualified: book strategy call via calendar
- If not qualified: politely decline with "We typically work with businesses spending $2K+/mo on marketing. When you're ready to invest at that level, please reach out!"
- Send case studies matching their industry

Tone: Professional B2B, direct, respectful of their time.

Sample qualifying questions:
1. "What type of business do you run?"
2. "What's your biggest marketing challenge right now?"
3. "Are you currently spending on marketing? Roughly what range?"
4. "Timeline - when do you hope to see results?"

---

## Integration Checkpoint

- [ ] Created AI agent in GHL
- [ ] System prompt configured with persona, rules, escalation
- [ ] Knowledge base uploaded (class schedule, FAQs, staff)
- [ ] Agent actions configured (book, tag, escalate)
- [ ] Ran 10+ test conversations
- [ ] Human handoff workflow built
- [ ] Tested escalation path
- [ ] Reviewed conversation logs

## Day 21 Recap Questions

1. What are GHL's four AI feature categories?
2. When should AI escalate to a human?
3. What are the four pillars of a system prompt?
4. How do you prevent AI hallucinations?
5. What should every AI agent test suite include?

## Next Day Preview

**Day 22: Advanced Automation Patterns** - Nested conditional logic, math operations, goal events, and intelligent lead routing. The expert patterns that separate power users from experts.
