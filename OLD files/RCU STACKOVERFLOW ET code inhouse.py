import xml.etree.ElementTree as ET

xml = '''<r>  <Learner>
        <LearnRefNumber>16Learner</LearnRefNumber>
        <PMUKPRN>87654321</PMUKPRN>
        <CampId>1234ABCD</CampId>
        <ULN>1061484016</ULN>
        <FamilyName>Smith</FamilyName>
        <GivenNames>Jane</GivenNames>
        <DateOfBirth>1999-02-27</DateOfBirth>
        <Ethnicity>31</Ethnicity>
        <Sex>F</Sex>
        <LLDDHealthProb>2</LLDDHealthProb>
        <Accom>5</Accom>
        <PlanLearnHours>440</PlanLearnHours>
        <PlanEEPHours>100</PlanEEPHours>
        <MathGrade>NONE</MathGrade>
        <EngGrade>D</EngGrade>
        <PostcodePrior>BR1 7SS</PostcodePrior>
        <Postcode>BR1 7SS</Postcode>
        <AddLine1>The Street</AddLine1>
        <AddLine2>ToyTown</AddLine2>
        <LearnerFAM>
            <LearnFAMType>LSR</LearnFAMType>
            <LearnFAMCode>55</LearnFAMCode>
        </LearnerFAM>
        <LearnerFAM>
            <LearnFAMType>EDF</LearnFAMType>
            <LearnFAMCode>2</LearnFAMCode>
        </LearnerFAM>
        <LearnerFAM>
            <LearnFAMType>MCF</LearnFAMType>
            <LearnFAMCode>3</LearnFAMCode>
        </LearnerFAM>
        <LearnerFAM>
            <LearnFAMType>FME</LearnFAMType>
            <LearnFAMCode>2</LearnFAMCode>
        </LearnerFAM>
        <LearnerFAM>
            <LearnFAMType>PPE</LearnFAMType>
            <LearnFAMCode>2</LearnFAMCode>
        </LearnerFAM>
        <!-- Employment status record is not required for full time 16-19 (excluding apprenticeships) funded learners  -->
        <!-- 16-19  (excluding apprenticeships) funded study programme -->
        <LearningDelivery>
            <LearnAimRef>50022246</LearnAimRef>
            <AimType>5</AimType>
            <AimSeqNumber>1</AimSeqNumber>
            <LearnStartDate>2015-09-14</LearnStartDate>
            <LearnPlanEndDate>2016-07-02</LearnPlanEndDate>
            <FundModel>25</FundModel>
            <DelLocPostCode>BR1 3RL</DelLocPostCode>
            <CompStatus>1</CompStatus>
            <SWSupAimId>cb5f0d25-cff4-4ea0-92f5-99378cce306d</SWSupAimId>
            <LearningDeliveryFAM>
                <LearnDelFAMType>SOF</LearnDelFAMType>
                <LearnDelFAMCode>107</LearnDelFAMCode>
            </LearningDeliveryFAM>
        </LearningDelivery>
        <LearningDelivery>
            <LearnAimRef>50023408</LearnAimRef>
            <AimType>4</AimType>
            <AimSeqNumber>2</AimSeqNumber>
            <LearnStartDate>2015-02-14</LearnStartDate>
            <LearnPlanEndDate>2016-07-15</LearnPlanEndDate>
            <FundModel>25</FundModel>
            <DelLocPostCode>BR2 7UP</DelLocPostCode>
            <CompStatus>3</CompStatus>
            <LearnActEndDate>2015-04-01</LearnActEndDate>
            <WithdrawReason>98</WithdrawReason>
            <Outcome>3</Outcome>
            <SWSupAimId>c243182a-30af-4879-8f68-3eac708e6bb3</SWSupAimId>
            <LearningDeliveryFAM>
                <LearnDelFAMType>SOF</LearnDelFAMType>
                <LearnDelFAMCode>107</LearnDelFAMCode>
            </LearningDeliveryFAM>
        </LearningDelivery>
    </Learner></r>
'''

root = ET.fromstring(xml)
dob_lst = root.findall('.//Learner/DateOfBirth')
for dob in dob_lst:
  dob.text = 'NULL'
ET.dump(root)


tree.write('output123.xml')
