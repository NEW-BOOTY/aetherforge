# Copyright © 2025 Devin B. Royal.
# All Rights Reserved.

from reportlab.lib.pagesizes import letter, A4
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import inch
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, PageBreak
from reportlab.lib.enums import TA_CENTER, TA_LEFT
from reportlab.pdfgen import canvas
import os

class AetherForgeQuoteGenerator:
    def __init__(self, output_path="AetherForge-Enterprise-Quote.pdf"):
        self.output_path = output_path
        self.doc = SimpleDocTemplate(output_path, pagesize=A4, rightMargin=72, leftMargin=72, topMargin=72, bottomMargin=18)
        self.story = []
        self.styles = getSampleStyleSheet()
        self.setup_styles()
        self.copyright = "Copyright © 2025 Devin B. Royal. All Rights Reserved."

    def setup_styles(self):
        # Custom header style
        self.header_style = ParagraphStyle(
            'CustomHeader',
            parent=self.styles['Heading1'],
            fontSize=24,
            spaceAfter=30,
            alignment=TA_CENTER,
            textColor=colors.darkblue
        )
        # Body text
        self.body_style = ParagraphStyle(
            'BodyText',
            parent=self.styles['Normal'],
            fontSize=11,
            spaceAfter=12,
            leftIndent=0
        )
        # Footer
        self.footer_style = ParagraphStyle(
            'Footer',
            parent=self.styles['Normal'],
            fontSize=9,
            alignment=TA_CENTER,
            spaceAfter=0,
            textColor=colors.grey
        )

    def add_header(self):
        self.story.append(Paragraph("AetherForge Enterprise License Quote", self.header_style))
        self.story.append(Spacer(1, 0.2*inch))
        self.story.append(Paragraph("<b>Issued to:</b> [Client Company Name]<br/>"
                                   "<b>Contact:</b> [Client Contact Name]<br/>"
                                   "<b>Date:</b> December 5, 2025<br/>"
                                   "<b>Issued by:</b> Devin Benard Royal, CTO<br/>"
                                   "AetherForge Platform<br/>"
                                   "<a href='https://github.com/new-booty/aetherforge'>github.com/new-booty/aetherforge</a>",
                                   self.body_style))
        self.story.append(Spacer(1, 0.3*inch))

    def add_overview(self):
        self.story.append(Paragraph("Quote Overview", self.styles['Heading2']))
        overview_text = """
        <p>This quote outlines enterprise licensing terms for AetherForge, the original, governed, monetizable platform providing runtime license enforcement, post-quantum cryptography (PQC) security, modular agent federation, immutable audit logging, and self-healing orchestration. All terms are governed by the End-User License Agreement (EULA) attached as Appendix A.</p>
        <p>AetherForge enables enterprises to deploy secure, compliant multi-agent systems with immediate revenue generation via tiered features. Key capabilities include:</p>
        <ul>
            <li>Runtime license validation (fail-closed on expiry/revocation)</li>
            <li>PQC primitives (Kyber512 key exchange, Dilithium2 signing) for quantum-resistant artifacts</li>
            <li>Immutable audit bus with one-click compliance exports (JSON/CSV)</li>
            <li>Self-healing deployments to Kubernetes/AWS/Azure/GCP with circuit breakers and rollbacks</li>
            <li>Monetization hooks for subscriptions/one-time purchases, integrated with Stripe</li>
        </ul>
        """
        self.story.append(Paragraph(overview_text, self.body_style))
        self.story.append(Spacer(1, 0.2*inch))

    def add_pricing_table(self):
        self.story.append(Paragraph("Pricing Tiers", self.styles['Heading2']))
        data = [
            ['Tier', 'Annual Fee', 'Key Features', 'Ideal For'],
            ['Starter', '$25,000', 'Unlimited agents, full PQC, basic audits, on-prem only', 'Mid-size teams scaling agents'],
            ['Unlimited', '$99,000', 'Multi-tenant, 99.99% SLA, custom compliance exports, priority support', 'Enterprise-wide adoption']
        ]
        table = Table(data)
        table.setStyle(TableStyle([
            ('BACKGROUND', (0, 0), (-1, 0), colors.grey),
            ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
            ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
            ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
            ('FONTSIZE', (0, 0), (-1, 0), 10),
            ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
            ('BACKGROUND', (0, 1), (-1, -1), colors.beige),
            ('GRID', (0, 0), (-1, -1), 1, colors.black)
        ]))
        self.story.append(table)
        self.story.append(Spacer(1, 0.3*inch))
        self.story.append(Paragraph("<i>Payment Terms:</i> 50% upon signature, 50% within 30 days. Invoicing via Stripe/ACH. Discounts: 10% for annual prepay; 15% for 3-year commitment.", self.body_style))

    def add_scope(self):
        self.story.append(Paragraph("Scope of License", self.styles['Heading2']))
        scope_text = """
        <ol>
            <li><b>Grant:</b> Non-exclusive, non-transferable license to use AetherForge software for internal business purposes, limited to the tier purchased.</li>
            <li><b>Restrictions:</b> No reverse engineering, redistribution, or modification. Violations trigger immediate revocation and liquidated damages of 3x license fee.</li>
            <li><b>Support & Maintenance:</b> Unlimited email/ticket support; major updates included. Custom integrations billed at $250/hour.</li>
            <li><b>Confidentiality:</b> All proprietary elements (source, keys, algorithms) treated as trade secrets under NDA.</li>
            <li><b>Warranty:</b> 90-day defect warranty; services provided "as-is" thereafter. Limitation of liability: Max license fee.</li>
            <li><b>Termination:</b> Upon material breach (30-day cure period); post-termination, cease use and destroy copies.</li>
        </ol>
        """
        self.story.append(Paragraph(scope_text, self.body_style))
        self.story.append(Spacer(1, 0.5*inch))

    def add_acceptance(self):
        self.story.append(Paragraph("Acceptance & Next Steps", self.styles['Heading2']))
        self.story.append(Paragraph("This quote is valid for 30 days. Upon acceptance, execute the signature block below and return via email. We will provision license keys and onboarding within 48 hours.", self.body_style))
        self.story.append(Spacer(1, 1*inch))
        sig_text = """
        <b>Signature Block</b><br/>
        <br/>
        Accepted by: ______________________________<br/>
        Name: ____________________________________<br/>
        Title: ___________________________________<br/>
        Date: ____________________________________<br/>
        <br/>
        Devin Benard Royal<br/>
        Chief Technology Officer<br/>
        AetherForge Platform<br/>
        Email: [your-email@example.com]<br/>
        Date: December 5, 2025
        """
        self.story.append(Paragraph(sig_text, self.body_style))
        self.story.append(Spacer(1, 0.5*inch))
        self.story.append(Paragraph("Appendix A: EULA.txt (embedded reference—full terms available upon request).", self.body_style))
        self.story.append(PageBreak())

    def add_appendix(self):
        self.story.append(Paragraph("Appendix A: End-User License Agreement (EULA) Summary", self.styles['Heading2']))
        eula_text = """
        <p>This EULA governs use of AetherForge software. Full text available at github.com/new-booty/aetherforge/EULA.txt.</p>
        <p><b>1. Definitions:</b> "Software" includes all binaries, source, documentation, and derivatives. "Authorized Users" limited to employees/contractors under the license tier.</p>
        <p><b>2. License Grant:</b> Subject to payment, Licensee receives a perpetual (for term), non-exclusive license for the purchased tier. Offline grace: 7 days.</p>
        <p><b>3. Intellectual Property:</b> All rights reserved by Devin B. Royal. Licensee acquires no ownership; grant is limited.</p>
        <p><b>4. Compliance & Audit:</b> Licensee consents to remote audits (quarterly, non-disruptive) for tier adherence. Violations: Immediate termination + damages.</p>
        <p><b>5. Security Obligations:</b> Licensee must implement reasonable safeguards; report breaches within 24 hours. PQC keys rotated quarterly.</p>
        <p><b>6. Indemnification:</b> Licensor indemnifies against IP claims on unmodified Software; Licensee indemnifies for misuse.</p>
        <p><b>7. Governing Law:</b> Laws of Delaware, USA. Disputes: Binding arbitration in San Francisco, CA.</p>
        <p><b>8. Entire Agreement:</b> This quote + EULA supersedes prior understandings. Amendments in writing only.</p>
        <p><i>Confidential: For [Client] Internal Use Only.</i></p>
        """
        self.story.append(Paragraph(eula_text, self.body_style))
        self.story.append(Spacer(1, 0.5*inch))
        self.story.append(Paragraph(self.copyright, self.footer_style))

    def generate(self):
        try:
            self.add_header()
            self.add_overview()
            self.add_pricing_table()
            self.add_scope()
            self.add_acceptance()
            self.add_appendix()
            self.doc.build(self.story)
            print(f"✓ PDF generated: {self.output_path} (2 pages)")
            os.system(f"open {self.output_path}")  # macOS preview
            return True
        except Exception as e:
            print(f"✗ Generation failed: {str(e)}")
            return False

if __name__ == "__main__":
    generator = AetherForgeQuoteGenerator()
    generator.generate()

# Copyright © 2025 Devin B. Royal.
# All Rights Reserved.